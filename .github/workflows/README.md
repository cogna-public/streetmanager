# GitHub Workflows Documentation

## Automated Version Bumping and Publishing

Releases run in two workflows. Both are gated by repository rules and environments managed in Terraform in `cogna-co/terraform`, so only reviewed code on `main` can publish.

### 1. `auto-version.yml` - Automatic Version Bumping

**Trigger:** Every push to `main`, or a manual run from `main` (`just release minor`)

**What it does:**
- Bumps the **patch version** (e.g., 0.5.11 → 0.5.12), or the part chosen on a manual run
- Runs `uv version --bump` to update `pyproject.toml` and `uv.lock`
- Commits the version change with message `publish: bump to vX.Y.Z`
- Creates a git tag `vX.Y.Z`
- Creates a GitHub release with notes generated from the commits since the last tag, or the notes given on a manual run

**Skip conditions:**
- Commit message starts with `publish:` (to avoid loops from the app's own commits)

**Authentication:**
- The job runs in the `release` environment, which only `main` can deploy to. It mints a short-lived token for the `cogna-package-releaser` GitHub App with `actions/create-github-app-token`.
- The app is the only actor the repository rules let push to `main` without a reviewed PR, and the only one allowed to create `v*` tags.
- A release created with the app token triggers `publish.yml`; one created with `GITHUB_TOKEN` would not.

### 2. `publish.yml` - PyPI Publishing

**Trigger:** GitHub release published (by `auto-version.yml`)

**What it does:**
- Builds source distribution and wheel using `uv build`
- Publishes to PyPI using Trusted Publishing (OIDC) from the `pypi` environment, which only `v*` tags can deploy to
- No API tokens required

## Usage

### Automatic Flow (Default)

Merge any PR to `main`:

1. Your PR gets merged to `main`
2. `auto-version.yml` bumps the patch version (0.5.11 → 0.5.12)
3. The app commits the version bump and creates a tag
4. The app creates a GitHub release
5. `publish.yml` is triggered and publishes to PyPI

### Manual Flow (For major/minor bumps)

Run `auto-version.yml` from `main` with the bump you want:

```bash
just release minor        # bump minor (0.5.x → 0.6.0)
just release major "Msg"  # bump major (0.5.x → 1.0.0)
```

Pushing a bump commit or a `v*` tag by hand is blocked by the repository rules.

## Setup

The `release` environment needs:

- variable `RELEASE_APP_CLIENT_ID`: the `cogna-package-releaser` app's client ID
- secret `RELEASE_APP_PRIVATE_KEY`: a private key for the app

The PyPI trusted publisher must name workflow `publish.yml` and environment `pypi`.

## Workflow Permissions

- `auto-version.yml`: `contents: read` for `GITHUB_TOKEN`; the app token, limited to `contents: write`, commits, tags and releases.
- `publish.yml`: `contents: read`, `id-token: write` for PyPI Trusted Publishing.

## Troubleshooting Cheatsheet

- Version bump skipped? Check the workflow log; the job ignores commits starting with `publish:`.
- Token step failed? Check that the `release` environment has `RELEASE_APP_CLIENT_ID` and `RELEASE_APP_PRIVATE_KEY`, and that the app is installed on this repository.
- Publish workflow missing? Confirm the release was published by the app, not with `GITHUB_TOKEN`.
- PyPI publish failed? Re-run `Publish` for the release once any OIDC/environment issues are resolved.

## Testing Changes

Neither workflow can do anything from a branch: `release` and `pypi` refuse branch deployments. Review workflow changes in the PR; the first merge to `main` exercises them.
