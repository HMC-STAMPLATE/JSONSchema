# JSONSchemas

This repo provides JSON Schema definitions for the `properties` objects of the
OGC STA entities `Thing`, `Sensor`, `Datastream`, `ObservedProperty`,
`Location`, `Observation` and `FeatureOfInterest`.


## Examples

The example folder provides example JSON-LD and schema.org compliant examples.

### Linting

To check JSON-LD compatibility it is possible to lint the examples with the
`jsonld-cli` tool:

```
npx jsonld-cli lint examples/thing_properties.json
```

