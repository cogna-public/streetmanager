# GitHub Workflows Documentation

## Automated Version Bumping and Publishing

Releases run in two workflows, after the tests in `test.yml` pass on `main`. Both release workflows are gated by repository rules and environments managed in Terraform in `cogna-co/terraform`, so only reviewed, tested code on `main` can publish.

### 1. `auto-version.yml` - Automatic Version Bumping

**Trigger:** Every push to `main`

**What it does:**
- Checks out the tip of `main` and waits for that commit's `Test` job to pass, polling once a minute for up to 30 minutes. If it fails, or never starts, the run fails and nothing is released.
- Finds everything merged since the last `v*` tag
- Bumps the **patch version** (e.g., 0.5.11 → 0.5.12), or the minor or major version when any of those PR titles ends with `[minor]` or `[major]` (major wins)
- Runs `uv version --bump --no-sync` to update `pyproject.toml` and `uv.lock`, in a step that has no token
- Commits the version change with message `publish: bump to vX.Y.Z`, and the PR titles as the body
- Creates a git tag `vX.Y.Z`
- Creates a GitHub release whose notes are that commit body

Only PR titles count: the repository squash-merges, and each squash commit's subject is its PR title. A marker counts only at the end of the title, before GitHub's ` (#N)` suffix, and in any case: `Add new endpoint [minor]` is a minor release, `Docs about [major] releases` is a patch. Titles starting with `Revert "` never count, and neither does a `[major]` in a PR description or a commit message inside the PR.

**Skip conditions:**
- The push was made by `cogna-package-releaser[bot]`, which is the app's own bump commit
- Nothing has been merged since the last tag, for example on a re-run after a successful release
- Only files under `.github/` changed since the last tag, for example a Dependabot action update. The next release includes those merges.

With no `v*` tag on `main`, the run fails rather than guess where the last release was.

The app's bump commits are found by their author, `<id>+cogna-package-releaser[bot]@users.noreply.github.com`, not by subject, so a PR titled `publish: bump to v...` is released like any other.

**Authentication:**
- The job runs in the `release` environment, which only `main` can deploy to. Once the tests have passed, it mints a short-lived token for the `cogna-package-releaser` GitHub App with `actions/create-github-app-token`.
- The app is the only actor the repository rules let push to `main` without a reviewed PR, and the only one allowed to create `v*` tags.
- A release created with the app token triggers `publish.yml`; one created with `GITHUB_TOKEN` would not.
- Only the steps that push, tag and release have the token. `uv` runs in a step without it, so a build dependency cannot push to `main`.
- The token is passed to each `git push` directly and never stored in `.git/config`.
- The workflow skips pushes by `cogna-package-releaser[bot]`, so the app's slug must stay `cogna-package-releaser`. If the app is renamed, update the `if:` in `auto-version.yml`.

### 2. `publish.yml` - PyPI Publishing

**Trigger:** GitHub release published (by `auto-version.yml`)

**What it does:**
- Builds source distribution and wheel using `uv build`
- Publishes to PyPI using Trusted Publishing (OIDC) from the `pypi` environment, which only `v*` tags can deploy to
- No API tokens required

### 3. `test.yml` - Tests

**Trigger:** Pull requests to `main`, and every push to `main`

Runs the test suite. The push run is the one `auto-version.yml` waits for, so a merge is tested as merged, not only as its PR branch. `auto-version.yml` matches the job by its name, `Test`, as reported by GitHub Actions, so renaming the job needs the same change to `checks_include` there.

## Usage

Merge any PR to `main`:

1. Your PR gets merged to `main`
2. `test.yml` runs on the merge, and `auto-version.yml` waits for it to pass
3. `auto-version.yml` bumps the version: patch by default, or minor or major if the PR title ends with `[minor]` or `[major]`
4. The app commits the version bump and creates a tag
5. The app creates a GitHub release
6. `publish.yml` is triggered and publishes to PyPI

For a minor or major release, put the marker in the PR title, for example `Add new endpoint [minor]`. No patch release goes out first.

Pushing a bump commit or a `v*` tag by hand is blocked by the repository rules.

## Setup

The `release` environment needs:

- variable `RELEASE_APP_CLIENT_ID`: the `cogna-package-releaser` app's client ID
- secret `RELEASE_APP_PRIVATE_KEY`: a private key for the app

The PyPI trusted publisher must name workflow `publish.yml` and environment `pypi`.

## Workflow Permissions

- `auto-version.yml`: `contents: read`, plus `checks: read` and `actions: read` so `allcheckspassed` can read the test results, for `GITHUB_TOKEN`. The app token, limited to `contents: write`, commits, tags and releases.
- `test.yml`: `contents: read`.
- `publish.yml`: no workflow-wide permissions. The `build` job has `contents: read`; the `publish-pypi` job has only `id-token: write`, for PyPI Trusted Publishing.

## When a release fails

Re-run the failed **Auto Version Bump** run. Each run releases whatever is unreleased, so a re-run is always safe:

- If the bump commit was pushed but the tag or release wasn't created, the re-run tags that commit and creates the release, without bumping again.
- If the push was rejected because another PR merged during the run, the run for that later merge releases both. If that run has already finished, re-run the failed one.
- GitHub keeps one pending run per workflow, so a run can be cancelled when several PRs merge close together. The next run still includes the cancelled merge, and its `[minor]` or `[major]` marker.

If the run failed waiting for the tests:

- **The tests failed on `main`:** fix them in a new PR. Its merge releases everything unreleased, including the merge whose tests failed.
- **A test was flaky, or the tests took longer than 30 minutes:** re-run the failed **Test** jobs, then re-run **Auto Version Bump** once they pass.
- **"Failing due to missing checks":** no `Test` job was found on the commit. Check that `test.yml` ran for that push.

If **Publish** fails (for example, an OIDC or trusted publisher problem), fix the cause and re-run the Publish run for that release.

Other first-run problems:

- **The token step fails:** check that the `release` environment has `RELEASE_APP_CLIENT_ID` and `RELEASE_APP_PRIVATE_KEY`, and that the app is installed on this repository.
- **Publish never starts:** the release must be created by the app. A release created with `GITHUB_TOKEN` does not trigger other workflows.
- **The app key is lost or leaked:** a `cogna-public` organisation owner generates a new private key in the app's settings, deletes the old one, and replaces `RELEASE_APP_PRIVATE_KEY` in the `release` environment. The rules and environments themselves are defined in `cogna-co/terraform`, in `modules/data/github/repositories/source/definitions/`.

## Testing Changes

Neither workflow can do anything from a branch: `release` and `pypi` refuse branch deployments. Review workflow changes in the PR; the first merge to `main` exercises them.
