# HMC STAMPLATE JSON-Schemas

This repo provides JSON-Schema definitions for the `properties` objects of the
OGC STA entities `Thing`, `Sensor`, `Datastream`, `ObservedProperty`,
`Location`, `Observation` and `FeatureOfInterest`.

## Goals

With this project we want to standardize the use of the freely definable
property `properties` of the OGC STA entities within the HMC STAMPLATE project.
For this purpose, JSON schemas are defined that enable the validation of these
properties on both the service and the client side. This ensures uniform access
to this data across the centers.

We also want to semantically label the data by using the terms already defined
at https://schema.org.

## Structure of this Repository

- `stamplate.jsonld`, contains the necessary adoptions and definitions of terms
    used in the JSON documents
- `schemas/`, contains the JSON-Schema definitions for each OGC STA entity
    property
- `examples/`, contains examples of JSON-Schema and JSON-LD valid documents for
    each OGC STA entity property

## Examples

The `examples` folder provides JSON-LD and schema.org compliant examples for the
mentioned properties.

## JSON-Schema Generation

To generate a base schema from an example, use:

```
npx generate-schema -j examples/thing_properties.json > example_thing_properties.schema.json
```

 ⚠️ Take care that the `"$schema"` property has the version `"http://json-schema.org/draft-06/schema#"`.

## JSON-Schema Validation

To validate the schemas, run

```
npm run lint:schemas
```

To validate the examples against the schemas, run

```
npm run lint:schemas-examples
```

## JSON-LD Compability

To check for JSON-LD compatibility lint the `stamplate.jsonld` context file
with:

```
npm run lint:jsonld
```

To check the examples for JSON-LD compatibility, run:

```
npm run lint:jsonld-examples
```

⚠️ The `json-ld` linter just takes care that the file is correct to the JSON-LD
specifications, it does not resolve or checks types from
[schema.org](https://schema.org).

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

## Authors

- @u.loup
- @marc.hanisch
