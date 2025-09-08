default:
  just --list

render api="work":
  docker run -it --rm -v $PWD:/app/ -w /app swaggerapi/swagger-codegen-cli-v3:3.0.68 generate \
      -i "https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/{{api}}-swagger.json" \
      -l python -o src/streetmanager/{{api}}

apis:
  rm -rf src/streetmanager/work/
  rm -rf src/streetmanager/geojson/
  rm -rf src/streetmanager/lookup/
  rm -rf src/streetmanager/party/
  rm -rf src/streetmanager/event/
  rm -rf src/streetmanager/reporting/
  rm -rf src/streetmanager/export/
  rm -rf src/streetmanager/sampling/
  just render work
  just render geojson
  just render lookup
  just render party
  just render event
  just render reporting
  just render export
  just render sampling
  uv run ./scripts/fix_swagger_imports.py
  uv run ./scripts/test_swagger_imports.py

# Run the smoke test suite with uv
test:
  uv run -m pytest -q

# Create a release: bump version with uv, tag, push, and create GitHub Release
# Usage examples:
#   just release                 # bump patch
#   just release minor           # bump minor
#   just release major "Notes"   # bump major with notes
release bump="patch" notes="":
  set -euo pipefail
  # Bump version using uv
  uv version --bump {{bump}}
  # Extract new version from pyproject.toml
  new_version=$(rg -n '^version\s*=\s*"([^"]+)"' -or '$1' pyproject.toml | head -n1)
  # Commit and push
  git add pyproject.toml
  git commit -m "publish: bump to v${new_version}" || echo "No changes to commit"
  git push origin main
  # Tag and push
  git tag "v${new_version}" || echo "Tag already exists"
  git push origin "v${new_version}" || echo "Tag push failed (may already exist)"
  # Prepare notes
  if [ -z "{{notes}}" ]; then rel_notes="Release v${new_version}"; else rel_notes="{{notes}}"; fi
  # Create GitHub Release
  gh release create "v${new_version}" --title "v${new_version}" --notes "${rel_notes}" --repo cogna-public/streetmanager || echo "Release may already exist"
