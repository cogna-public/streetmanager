# GitHub Workflows Documentation

## Automated Version Bumping and Publishing

Releases run in two workflows. Both are gated by repository rules and environments managed in Terraform in `cogna-co/terraform`, so only reviewed code on `main` can publish.

### 1. `auto-version.yml` - Automatic Version Bumping

**Trigger:** Every push to `main`

**What it does:**
- Checks out the tip of `main` and finds everything merged since the last `v*` tag
- Bumps the **patch version** (e.g., 0.5.11 → 0.5.12), or the minor or major version when any of those PR titles contains `[minor]` or `[major]` (major wins)
- Runs `uv version --bump` to update `pyproject.toml` and `uv.lock`
- Commits the version change with message `publish: bump to vX.Y.Z`
- Creates a git tag `vX.Y.Z`
- Creates a GitHub release listing the PR titles since the last tag

Only PR titles count: the repository squash-merges, and each squash commit's subject is its PR title. A `[major]` in a PR description or a commit message inside the PR is ignored.

**Skip conditions:**
- The push was made by `cogna-package-releaser[bot]`, which is the app's own bump commit
- Nothing has been merged since the last tag, for example on a re-run after a successful release

**Authentication:**
- The job runs in the `release` environment, which only `main` can deploy to. It mints a short-lived token for the `cogna-package-releaser` GitHub App with `actions/create-github-app-token`.
- The app is the only actor the repository rules let push to `main` without a reviewed PR, and the only one allowed to create `v*` tags.
- A release created with the app token triggers `publish.yml`; one created with `GITHUB_TOKEN` would not.
- The token is passed to each `git push` directly and never stored in `.git/config`.

### 2. `publish.yml` - PyPI Publishing

**Trigger:** GitHub release published (by `auto-version.yml`)

**What it does:**
- Builds source distribution and wheel using `uv build`
- Publishes to PyPI using Trusted Publishing (OIDC) from the `pypi` environment, which only `v*` tags can deploy to
- No API tokens required

## Usage

Merge any PR to `main`:

1. Your PR gets merged to `main`
2. `auto-version.yml` bumps the version: patch by default, or minor or major if the PR title says `[minor]` or `[major]`
3. The app commits the version bump and creates a tag
4. The app creates a GitHub release
5. `publish.yml` is triggered and publishes to PyPI

For a minor or major release, put the marker in the PR title, for example `Add new endpoint [minor]`. No patch release goes out first.

Pushing a bump commit or a `v*` tag by hand is blocked by the repository rules.

## Setup

The `release` environment needs:

- variable `RELEASE_APP_CLIENT_ID`: the `cogna-package-releaser` app's client ID
- secret `RELEASE_APP_PRIVATE_KEY`: a private key for the app

The PyPI trusted publisher must name workflow `publish.yml` and environment `pypi`.

## Workflow Permissions

- `auto-version.yml`: `contents: read` for `GITHUB_TOKEN`. The app token, limited to `contents: write`, commits, tags and releases.
- `publish.yml`: no workflow-wide permissions. The `build` job has `contents: read`; the `publish-pypi` job has only `id-token: write`, for PyPI Trusted Publishing.

## When a release fails

Re-run the failed **Auto Version Bump** run. Each run releases whatever is unreleased, so a re-run is always safe:

- If the bump commit was pushed but the tag or release wasn't created, the re-run tags that commit and creates the release, without bumping again.
- If the push was rejected because another PR merged during the run, the run for that later merge releases both. If that run has already finished, re-run the failed one.
- GitHub keeps one pending run per workflow, so a run can be cancelled when several PRs merge close together. The next run still includes the cancelled merge, and its `[minor]` or `[major]` marker.

If **Publish** fails (for example, an OIDC or trusted publisher problem), fix the cause and re-run the Publish run for that release.

## Testing Changes

Neither workflow can do anything from a branch: `release` and `pypi` refuse branch deployments. Review workflow changes in the PR; the first merge to `main` exercises them.
