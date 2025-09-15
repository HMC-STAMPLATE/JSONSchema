# Enhanced STA Properties

The `properties` objects in the respective OGC STA entities are populated with
additional information that is difficult or impossible to represent with the
current STA data model ([OGC SensorThings API Part 1: Sensing Version 1.1](https://docs.ogc.org/is/18-088/18-088.html)).

The provided data structures use [JSON-LD](https://json-ld.org/) and are loosely
based on [schema.org](https://schema.org). A corresponding [JSON
Schema](https://json-schema.org/) has been created on each `properties` object.

## The enhanced *Thing*

```{table} Table 1: The Thing properties
:name: tbl-thing-properties
:class: thing-table
:align: left

| *Name* | Definition | Data type | Multiplicity and use |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | String/Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used (schema.org). | String | One (mandatory) |
| `jsonld.id` | Unique ID of the object. | String | (One) mandatory |
| `jsonld.type` | The type of the object, in this case 'ThingProperties'. | String | One (mandatory) |
| `identifier` | Another unique identifier for the object, eg. a PID. | String | Zero-to-one |
| `responsiblePersons` | A list of persons responsible for the object. | Array of Objects | Zero-to-many |
| `responsiblePersons.jsonld.type` | The type of the object, in this case 'Role'. | String | One (mandatory) |
| `responsiblePersons.roleName` | The name of the role (e.g., 'Owner'). | String | Zero-to-one |
| `responsiblePersons.definition` | URL to the definition of the role. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons` | A nested list of person objects fulfilling the role. | Array of Objects | Zero-to-many |
| `responsiblePersons.responsiblePersons.jsonld.id` | Unique ID of the person. | String | One (mandatory) |
| `responsiblePersons.responsiblePersons.jsonld.type` | The type of the object, in this case 'Person'. | String | One (mandatory) |
| `responsiblePersons.responsiblePersons.givenName` | The person's given name. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.familyName` | The person's family name. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.email` | The person's email address. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation` | The organization the person is affiliated with. | Object | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation.jsonld.type` | The type of the object, in this case 'Organization'. | String | One (mandatory) |
| `responsiblePersons.responsiblePersons.affiliation.name` | Name of the organization. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation.identifier` | Unique identifier of the organization. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.identifier` | Unique identifier of the person (e.g., ORCID). | String | Zero-to-one |
| `partOfProjects` | A list of projects this object belongs to. | Array of Objects | Zero-to-many |
| `partOfProjects.jsonld.type` | The type of the object, in this case 'ResearchProject'. | String | One (mandatory) |
| `partOfProjects.name` | Name of the project. | String | Zero-to-one |
| `images` | A list of images linked to the object. | Array of Objects | Zero-to-many |
| `images.@type` | The type of the object, in this case 'ImageObject'. | String | One (mandatory) |
| `images.caption` | A short caption for the image. | String | Zero-to-one |
| `images.contentUrl` | The URL where the image can be accessed. | String | Zero-to-one |
| `metadata` | Metadata for the object. | Object | Zero-to-one |
| `metadata.jsonld.type` | The type of the object, in this case 'Dataset'. | String | One (mandatory) |
| `metadata.encodingType` | The encoding type of the dataset. | String | Zero-to-one |
| `metadata.distribution` | Information about the dataset's distribution. | Object | Zero-to-one |
| `metadata.distribution.jsonld.type` | The type of the object, in this case 'DataDownload'. | String | One (mandatory) |
| `metadata.distribution.url` | The URL to download the dataset. | String | Zero-to-one |
| `sourceRelatedThings` | A list of related things from which this object originates. | Array of Objects | Zero-to-many |
| `sourceRelatedThings.jsonld.id` | Unique ID of the related object. | String | One (mandatory) |
| `sourceRelatedThings.jsonld.type` | The type of the object, in this case 'RelatedThing'. | String | One (mandatory) |
| `sourceRelatedThings.relationRole` | The role the object plays in the relationship. | Object | Zero-to-one |
| `sourceRelatedThings.relationRole.jsonld.type` | The type of the object, in this case 'RelationRole'. | String | One (mandatory) |
| `sourceRelatedThings.relationRole.name` | The name of the relationship (e.g., 'containedInPlace'). | String | Zero-to-one |
| `sourceRelatedThings.relationRole.definition` | URL to the definition of the relationship. | String | Zero-to-one |
| `sourceRelatedThings.relationRole.inverseName` | The name of the inverse relationship. | String | Zero-to-one |
| `sourceRelatedThings.relationRole.inverseDefinition` | URL to the definition of the inverse relationship. | String | Zero-to-one |
```

*Example*: ...

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "jsonld.id": "https://sensors.gfz.de/configurations/35",
  "jsonld.type": "ThingProperties",
  "identifier": "https://handle.net/12345",
  "responsiblePersons": [
    {
      "jsonld.type": "Role",
      "roleName": "Owner",
      "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/contactroles/4",
      "responsiblePersons": [
        {
          "jsonld.id": "https://sensors.gfz.de/contacts/49",
          "jsonld.type": "Person",
          "givenName": "Peter",
          "familyName": "Technician",
          "email": "christian.wille@gfz.de",
          "affiliation": {
            "jsonld.type": "Organization",
            "name": "Helmholtz Centre Potsdam German Research Centre for Geosciences GFZ",
            "identifier": "https://ror.org/04z8jg394"
          },
          "identifier": "https://orcid.org/0000-0003-0930-6527"
        }
      ]
    }
  ],
  "partOfProjects": [
    {
      "jsonld.type": "ResearchProject",
      "name": "TERENO-NO"
    }
  ],
  "images": [
    {
      "@type": "ImageObject",
      "caption": "Echo Sound Transducer at backside of Speedboat",
      "contentUrl": "https://sensors.gfz.de/backend/api/v1/configuration-attachments/2/file/IMG_20231204_144945_Echo_Sounder.jpg"
    },
    {
      "@type": "ImageObject",
      "caption": "Platform in situ",
      "contentUrl": "https://sensors.gfz.de/backend/api/v1/configuration-attachments/3/file/IMG_1451_Speedboat_platform_in_situ.jpg"
    }
  ],
  "metadata": {
    "jsonld.type": "Dataset",
    "encodingType": "http://www.opengis.net/doc/IS/SensorML/2.0",
    "distribution": {
      "jsonld.type": "DataDownload",
      "url": "https://sensors.gfz.de/backend/api/v1/devices/1/sensorml"
    }
  },
  "sourceRelatedThings": [
    {
      "jsonld.id": "https://sta.gfz.de/v1.1/Things(1)",
      "jsonld.type": "RelatedThing",
      "relationRole": {
        "jsonld.type": "RelationRole",
        "name": "containedInPlace",
        "definition": "https://schema.org/containedInPlace",
        "inverseName": "containsPlace",
        "inverseDefinition": "https://schema.org/containsPlace"
      }
    }
  ]
}
```

## The enhanced *Sensor*

TBA
