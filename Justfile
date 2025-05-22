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
  just render work
  just render geojson
  just render lookup
  just render party
  uv run ./scripts/fix_swagger_imports.py
  uv run ./scripts/test_swagger_imports.py

publish:
  rm -rf dist/ build/ src/*.egg-info/
  uv build
  uv publish
