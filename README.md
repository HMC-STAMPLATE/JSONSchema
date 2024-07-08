# JSONSchemas

This repo provides JSON Schema definitions for the `properties` objects of the
OGC STA entities `Thing`, `Sensor`, `Datastream`, `ObservedProperty`,
`Location`, `Observation` and `FeatureOfInterest`.

## Schema Generation

To generate a base schema from an example, use:

```
npx generate-schema -j examples/thing_properties.json > example_thing_properties.schema.json
```

 ⚠️ Take care that the `"$schema"` property has the version `"http://json-schema.org/draft-06/schema#"`.

## Schema Validation

```
npx ajv-cli validate -s schemas/thing_properties.schema.json -d
examples/thing_properties.json
```

## Examples

The `examples` folder provides JSON-LD and schema.org compliant examples for the
mentioned properties.

### JSON-LD Compability

To check for JSON-LD compatibility lint the examples with the
`jsonld-cli` tool:

```
npx jsonld-cli lint examples/thing_properties.json
```

To see if the terms are correctly resolved, expand the examples with the
`jsonld-cli` tool:

```
npx jsonld-cli expand examples/thing_properties.json
```

which generates the following result:

```json
[
  {
    "@id": "https://sensors.gfz-potsdam.de/configurations/35",
    "@type": [
      "https://codebase.helmholtz.cloud/stamplate/vocab/ThingProperties"
    ],
    "http://schema.org/identifier": [
      {
        "@value": "https://handle.net/12345"
      }
    ],
    "http://schema.org/dataset": [
      {
        "@type": [
          "http://schema.org/Dataset"
        ],
        "http://schema.org/distribution": [
          {
            "@type": [
              "http://schema.org/DataDownload"
            ],
            "http://schema.org/url": [
              {
                "@value": "https://sensors.gfz-potsdam.de/backend/api/v1/devices/1/sensorml"
              }
            ]
          }
        ],
        "http://schema.org/encodingFormat": [
          {
            "@value": "http://www.opengis.net/doc/IS/SensorML/2.0"
          }
        ]
      }
    ],
    "http://schema.org/memberOf": [
      {
        "@type": [
          "http://schema.org/ResearchProject"
        ],
        "http://schema.org/name": [
          {
            "@value": "TERENO-NO"
          }
        ]
      }
    ],
    "http://schema.org/providerMobility": [
      {
        "@value": "static"
      }
    ],
    "http://schema.org/member": [
      {
        "@type": [
          "http://schema.org/Role"
        ],
        "http://schema.org/member": [
          {
            "@id": "https://sensors.gfz-potsdam.de/contacts/49",
            "@type": [
              "http://schema.org/Person"
            ],
            "http://schema.org/affiliation": [
              {
                "@type": [
                  "http://schema.org/Organization"
                ],
                "http://schema.org/identifier": [
                  {
                    "@value": "https://ror.org/04z8jg394"
                  }
                ],
                "http://schema.org/name": [
                  {
                    "@value": "Helmholtz Centre Potsdam German Research Centre for Geosciences GFZ"
                  }
                ]
              }
            ],
            "http://schema.org/email": [
              {
                "@value": "christian.wille@gfz-potsdam.de"
              }
            ],
            "http://schema.org/familyName": [
              {
                "@value": "Wille"
              }
            ],
            "http://schema.org/givenName": [
              {
                "@value": "Christian"
              }
            ],
            "http://schema.org/identifier": [
              {
                "@value": "https://orcid.org/0000-0003-0930-6527"
              }
            ]
          }
        ],
        "http://schema.org/roleName": [
          {
            "@value": "Owner"
          }
        ]
      }
    ],
    "http://schema.org/status": [
      {
        "@value": "active"
      }
    ]
  }
]
```

