# HMC STAMPLATE JSON Schemas

This repository provides JSON Schema definitions for the `properties` objects of the
OGC STA entities `Thing`, `Sensor`, `Datastream`, `ObservedProperty`,
`Location` and `Observation`.

## Goals

With this project we want to standardize the use of the freely definable
property `properties` of the [OGC
STA](https://www.ogc.org/standards/sensorthings/) entities within the [HMC
STAMPLATE](https://helmholtz-metadaten.de/inf-projects/stamplate) project.
For this purpose, JSON schemas are defined that enable the validation of these
properties on both the service and the client side. This ensures uniform access
to this data across the centers.

We also want to semantically label the data by using the terms already defined
at, e.g., https://schema.org.

## Structure of this Repository

- `stamplate.jsonld` contains the necessary adoptions and definitions of terms
    used in the JSON documents
- `schemas/` contains the JSON-Schema definitions for each OGC STA entity
    property
- `examples/` contains JSON-Schema and JSON-LD valid documents examples for
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

## JSON-LD Compatibility

To check for JSON-LD compatibility lint the `stamplate.jsonld` context file
with:

```
npm run lint:jsonld
```

To check the examples for JSON-LD compatibility, run:

```
npm run lint:jsonld-examples
```

⚠️ The `json-ld` linter ensures that the file is formatted correctly according to JSON-LD specifications.
specifications. It does not resolve or check types from
[schema.org](https://schema.org).

⚠️ The examples refer to the remote resource of the `stamplate.jsonld`
definition. If you have made changes to the local definition and want to test it
against the examples, be sure you refer to the local file.

To see if the terms are correctly resolved, expand the examples with the
`jsonld-cli` tool:

```
npx jsonld-cli expand examples/thing_properties.json
```

which generates the following result:

```json
[
  {
    "@id": "https://sensors.gfz.de/configurations/35",
    "@type": [
      "https://hmc-stamplate.github.io/JSONSchema/jsonld/ThingProperties"
    ],
    "http://schema.org/identifier": [
      {
        "@value": "https://handle.net/12345"
      }
    ],
    "http://schema.org/image": [
      {
        "http://schema.org/caption": [
          {
            "@value": "Echo Sound Transducer at backside of Speedboat"
          }
        ],
        "http://schema.org/contentUrl": [
          {
            "@value": "https://sensors.gfz.de/backend/api/v1/configuration-attachments/2/file/IMG_20231204_144945_Echo_Sounder.jpg"
          }
        ],
        "@type": [
          "http://schema.org/ImageObject"
        ]
      },
      {
        "http://schema.org/caption": [
          {
            "@value": "Platform in situ"
          }
        ],
        "http://schema.org/contentUrl": [
          {
            "@value": "https://sensors.gfz.de/backend/api/v1/configuration-attachments/3/file/IMG_1451_Speedboat_platform_in_situ.jpg"
          }
        ],
        "@type": [
          "http://schema.org/ImageObject"
        ]
      }
    ],
    "http://schema.org/dataset": [
      {
        "http://schema.org/distribution": [
          {
            "@type": [
              "http://schema.org/DataDownload"
            ],
            "http://schema.org/url": [
              {
                "@value": "https://sensors.gfz.de/backend/api/v1/devices/1/sensorml"
              }
            ]
          }
        ],
        "http://schema.org/encodingFormat": [
          {
            "@value": "http://www.opengis.net/doc/IS/SensorML/2.0"
          }
        ],
        "@type": [
          "http://schema.org/Dataset"
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
    "http://schema.org/member": [
      {
        "http://schema.org/sameAs": [
          {
            "@value": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/contactroles/4"
          }
        ],
        "@type": [
          "http://schema.org/Role"
        ],
        "http://schema.org/member": [
          {
            "http://schema.org/affiliation": [
              {
                "http://schema.org/identifier": [
                  {
                    "@value": "https://ror.org/04z8jg394"
                  }
                ],
                "@type": [
                  "http://schema.org/Organization"
                ],
                "http://schema.org/name": [
                  {
                    "@value": "GFZ Helmholtz Centre for Geosciences"
                  }
                ]
              }
            ],
            "http://schema.org/email": [
              {
                "@value": "john.doe@example.org"
              }
            ],
            "http://schema.org/familyName": [
              {
                "@value": "Doe"
              }
            ],
            "http://schema.org/givenName": [
              {
                "@value": "John"
              }
            ],
            "http://schema.org/identifier": [
              {
                "@value": "https://orcid.org/0000-0000-0000-1234"
              }
            ],
            "@id": "https://sensors.gfz.de/contacts/12345",
            "@type": [
              "http://schema.org/Person"
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
    "https://hmc-stamplate.github.io/JSONSchema/jsonld/sourceRelatedThings": [
      {
        "@id": "https://sta.gfz.de/v1.1/Things(1)",
        "@type": [
          "https://hmc-stamplate.github.io/JSONSchema/jsonld/RelatedThing"
        ],
        "https://hmc-stamplate.github.io/JSONSchema/jsonld/relationRole": [
          {
            "http://schema.org/sameAs": [
              {
                "@value": "https://schema.org/containedInPlace"
              }
            ],
            "https://hmc-stamplate.github.io/JSONSchema/jsonld/inverseDefinition": [
              {
                "@value": "https://schema.org/containsPlace"
              }
            ],
            "https://hmc-stamplate.github.io/JSONSchema/jsonld/inverseName": [
              {
                "@value": "containsPlace"
              }
            ],
            "@type": [
              "https://hmc-stamplate.github.io/JSONSchema/jsonld/RelationRole"
            ],
            "http://schema.org/name": [
              {
                "@value": "containedInPlace"
              }
            ]
          }
        ]
      }
    ]
  }
]
```

## Authors

- [Ulrich Loup](https://orcid.org/0009-0005-1370-6226)
- [Marc Hanisch](https://orcid.org/0000-0001-5272-4674)
- [Nils Brinckmann](https://orcid.org/0000-0001-8159-3888)
- [Class Faber](https://orcid.org/0000-0002-4861-3338)
- [David Schäfer](https://orcid.org/0000-0003-4517-6459)
- [Christof Lorenz](https://orcid.org/0000-0001-5590-5470)
