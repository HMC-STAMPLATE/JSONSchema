# Enhanced STA Properties

The goal of our extended STA profile is to enhance the basic STA data model (as shown in chapter ...) with additional information, that improves the FAIRness, transparency and consistency of sensor-related information particularly for applications in environmental sciences. For this, our approach was to model this additional information as `properties`, that are (according to the STA-standard) the natural place for any user-defined attributes. We, on purpose, did not want to introduce new entities and relationships, as STA-clients must be adapted for reading this additional information and this would introduce another level of complexity in the very simple and highly flexible STA base model.

## JSON-Schemas

- Write something about JSON-LD and JSON-Schemas and why we have chosen this approach for modeling our additonal information
  
## The enhanced *Thing*

| *Property*            | Definition                                                  | DataType                                   |
|-----------------------|-------------------------------------------------------------|--------------------------------------------|
| `@id`                 | ID of metadata source                                       | URI                                        |
| `partOfProjects`      | Related Projects and Campaigns                              | JSON Object                                |
| `identifier`          | (If available) PID of Thing (e.g, B2INST-handle)            | URL                                        |
| `metadata`            | Full dump of Thing-metadata in SensorML                     | DataType                                   |
| `sourceRelatedThings` | Relation between Things (e.g., within the same network)     | JSON Object                                |
| `responsiblePersons`  | Contact persons                                             | JSON Object                                |

Example: 

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "jsonld.id": "https://sensors.gfz-potsdam.de/configurations/35",
  "jsonld.type": "ThingProperties",
  "identifier": "https://handle.net/12345",
  "responsiblePersons": [
    {
      "jsonld.type": "Role",
      "roleName": "Owner",
      "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/contactroles/4",
      "responsiblePersons": [
        {
          "jsonld.id": "https://sensors.gfz-potsdam.de/contacts/49",
          "jsonld.type": "Person",
          "givenName": "Christian",
          "familyName": "Wille",
          "email": "christian.wille@gfz-potsdam.de",
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
      "contentUrl": "https://sensors.gfz-potsdam.de/backend/api/v1/configuration-attachments/2/file/IMG_20231204_144945_Echo_Sounder.jpg"
    },
    {
      "@type": "ImageObject",
      "caption": "Platform in situ",
      "contentUrl": "https://sensors.gfz-potsdam.de/backend/api/v1/configuration-attachments/3/file/IMG_1451_Speedboat_platform_in_situ.jpg"
    }
  ],
  "metadata": {
    "jsonld.type": "Dataset",
    "encodingType": "http://www.opengis.net/doc/IS/SensorML/2.0",
    "distribution": {
      "jsonld.type": "DataDownload",
      "url": "https://sensors.gfz-potsdam.de/backend/api/v1/devices/1/sensorml"
    }
  },
  "sourceRelatedThings": [
    {
      "jsonld.id": "https://sta.gfz-potsdam.de/v1.1/Things(1)",
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
