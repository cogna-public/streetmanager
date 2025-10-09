# GitHub Workflows Documentation

## Automated Version Bumping and Publishing

This repository uses a fully automated two-stage workflow for releases:

### 1. `auto-version.yml` - Automatic Version Bumping

**Trigger:** Every push to `main` branch

**What it does:**
- Automatically bumps the **patch version** (e.g., 0.5.11 → 0.5.12)
- Runs `uv version --bump patch` to update `pyproject.toml` and `uv.lock`
- Commits the version change with message `publish: bump to vX.Y.Z`
- Creates a git tag `vX.Y.Z`
- Creates a GitHub release with auto-generated notes from commits

**Skip conditions:**
- Commit message starts with `publish:` (to avoid infinite loops from the bot's own commits)

**Authentication:**
- The workflow prefers the repository secret `PAT_TOKEN` for git pushes, tags, and release creation so the downstream publish workflow is triggered.
- If `PAT_TOKEN` is absent, it falls back to `GITHUB_TOKEN`; the release is still created, but GitHub suppresses release-triggered workflows such as `publish.yml`.

**No special requirements:**
- No conventional commit format needed
- No PR labels needed
- Just merge to main and it happens automatically

### 2. `publish.yml` - PyPI Publishing

**Trigger:** GitHub release published (automatically triggered by auto-version workflow)

**What it does:**
- Builds source distribution and wheel using `uv build`
- Publishes to PyPI using Trusted Publishing (OIDC)
- No API tokens required

## Usage

### Automatic Flow (Default)

Simply merge any PR to `main`:

1. Your PR gets merged to `main`
2. `auto-version.yml` automatically bumps patch version (0.5.11 → 0.5.12)
3. Bot commits the version bump and creates a tag
4. Bot creates a GitHub release
5. `publish.yml` is triggered and publishes to PyPI

**That's it! No manual steps required.**

### Manual Flow (For major/minor bumps)

For **minor** or **major** version bumps, use the manual approach:

```bash
just release minor        # bump minor (0.5.x → 0.6.0)
just release major "Msg"  # bump major (0.5.x → 1.0.0)
```

Or disable `auto-version.yml` and always use manual releases.

## Quick Setup

- Add a fine-grained PAT with `contents: read/write` as the `PAT_TOKEN` repository secret (Actions → Secrets); it is used for release creation so the publish workflow fires.
- Keep the `pypi` environment configured for Trusted Publishing (OIDC) if you want review gates.
- That is all that is required for merges to `main` to build and publish.

## Workflow Permissions

- `auto-version.yml`: `contents: write` to commit, tag, and release.
- `publish.yml`: `contents: read`, `id-token: write` for PyPI Trusted Publishing.

## Troubleshooting Cheatsheet

- Version bump skipped? Check the workflow log; the job ignores commits starting with `publish:`.
- Publish workflow missing? Confirm the release was published and that `PAT_TOKEN` exists.
- PyPI publish failed? Re-run `Publish` with the saved tag once any OIDC/environment issues are resolved.

## Testing Changes

To test workflow changes without affecting version:

1. Create a feature branch
2. Modify workflow files
3. Test using `workflow_dispatch` trigger or in a fork
4. Merge when confident

Or temporarily add `workflow_dispatch:` trigger to test manually.
