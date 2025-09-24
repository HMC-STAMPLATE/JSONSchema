# Usage of the enhanced STA Profile
After explaining the additional attributes of our enhanced STA-Profile, we would like to present an actual use-case and how we can actually apply our profile. 

In the repository, you can find the two folders `schemas` and `examples`. The first contains the actual JSON-Schemas with detailed definitions, encodings, types and some controlled vocabulatires for all additional attributes. These can be seen as *rulebooks* or *templates* for our enhanced STA-profile against which I can validate a specific STA-ressource.

The latter holds examples for each entity, that fulfull exactly these guidelines.

## Infer an empty template or schema from an example

If you start from scratch and I just want an empty JSON-file that is consistent with our enhanced STAMPLATE-profile, I can simply run

```BASH
npx generate-schema -j examples/thing_properties.json > example_thing_properties.schema.json
```

This takes a pre-filled example, extracts the schema from this JSON and writes the extracted schema to a new file. This can then manually filled!

## Validate a STA-entity against our enhanced profile

Usually, a STA-ressource is available via an STA-Endpoint (e.g., https://sta.gfz.de/v1.1/Things(1)). Here is a simple workflow for validating such an entity against our JSON-Schemas:

1. Download the entity 

```BASH
curl -fsSL "https://sta.gfz.de/v1.1/Things(1)" -o tmp/thing_raw.json
```

2. Extract the properties

```BASH
jq '.properties' thing_raw.json > thing_properties.json
```

3. (Optional) Normalize `images` to match your schema:
If STA-JSONs are retrieved from some of our endpoints, several attributes had to be renamed (e.g., `@type` to `jsonld.type`). With this step, we transform the names back to the original schema-names. 

```BASH
jq '
  if (.images? | type) == "array" then
    .images = (.images | map(
      .["@type"]      = (."@type" // .["jsonld.type"]) |
      .contentUrl     = (.contentUrl // .url) |
      del(.["jsonld.type"], .url)
    ))
  elif (.images? | type) == "object" then
    .images = (
      .images
      | .["@type"]  = (.["@type"] // .["jsonld.type"])
      | .contentUrl = (.contentUrl // .url)
      | del(.["jsonld.type"], .url)
    )
  else . end
' thing_properties.json > thing_properties.norm.json
```

1. Validate the extracted and normalized properties against our Schema:

```
npm run validate -- -s schemas/thing_properties.schema.json -d thing_properties.norm.json
```
