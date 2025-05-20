


default:
  just --list

render api="work":
  docker run -it --rm -v $PWD:/app/ -w /app swaggerapi/swagger-codegen-cli-v3:3.0.68 generate \
      -i "https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/{{api}}-swagger.json" \
      -l python -o src/streetmanager/{{api}}

apis:
  just render work
  just render geojson
  just render lookup

