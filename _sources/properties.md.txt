# Enhanced STA Properties

The `properties` objects in the respective OGC STA entities are populated with
additional information that is difficult or impossible to represent with the
current STA data model ([OGC SensorThings API Part 1: Sensing Version 1.1](https://docs.ogc.org/is/18-088/18-088.html)).

The provided data structures use [JSON-LD](https://json-ld.org/) and are loosely
based on [schema.org](https://schema.org). A corresponding [JSON
Schema](https://json-schema.org/) has been created on each `properties` object.

## *Thing* properties 

The `ThingProperties` schema definition serves as a structured extension for the
OGC SensorThings API (STA) `Thing` entity. This schema allows for the enrichment
of `Thing` entities with critical information, such as persistent identifiers
(PIDs) for the Thing itself, details about the individuals or organizations
responsible for the Thing including roles and affiliations, links to projects
the Thing is associated with, a collection of images for visual documentation,
links to external metadata records and data distributions like SensorML
documents, and relationships to other Things, such as a sensor's relationship
to a platform.

```{table} Table 1: The Thing properties
:name: tbl-enhanced-thing-properties
:class: thing-table
:align: left

| *Name* | Definition | Data type | Multiplicity and use |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | String/Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used (schema.org). | String | One (mandatory) |
| `jsonld.id` | Unique ID of the object (e.g., the URL to its representation in an application). | String | (One) mandatory |
| `jsonld.type` | The type of the object, in this case 'ThingProperties'. | String | One (mandatory) |
| `identifier` | Another unique identifier for the object, eg. a PID. | String | Zero-to-one |
| `responsiblePersons` | A list of persons responsible for the object. | Array of [Role](https://schema.org/Role)-Objects | Zero-to-many |
| `responsiblePersons["jsonld.type"]` | The type of the object, in this case 'Role'. | String | One (mandatory) |
| `responsiblePersons.roleName` | The name of the role (e.g., 'Owner'). | String | Zero-to-one |
| `responsiblePersons.definition` | URL to the definition of the role. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons` | A nested list of person objects fulfilling the role. | Array of [Person](https://schema.org/Person)-Objects | Zero-to-many |
| `responsiblePersons.responsiblePersons["jsonld.id"]` | Unique ID of the person (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `responsiblePersons.responsiblePersons["jsonld.type"]` | The type of the object, in this case 'Person'. | String | One (mandatory) |
| `responsiblePersons.responsiblePersons.givenName` | The person's given name. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.familyName` | The person's family name. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.email` | The person's email address. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation` | The organization the person is affiliated with. | [Organization](https://schema.org/Organization)-Object | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation["jsonld.type"]` | The type of the object, in this case 'Organization'. | String | One (mandatory) |
| `responsiblePersons.responsiblePersons.affiliation.name` | Name of the organization. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation.identifier` | Unique identifier of the organization (e.g., ROR). | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.identifier` | Unique identifier of the person (e.g., ORCID). | String | Zero-to-one |
| `partOfProjects` | A list of projects this object belongs to. | Array of [ResearchProject](https://schema.org/ResearchProject)-Objects | Zero-to-many |
| `partOfProjects["jsonld.type"]` | The type of the object, in this case 'ResearchProject'. | String | One (mandatory) |
| `partOfProjects.name` | Name of the project. | String | Zero-to-one |
| `images` | A list of images linked to the object. | Array of [ImageObject](https://schema.org/ImageObject)-Objects | Zero-to-many |
| `images.@type` | The type of the object, in this case 'ImageObject'. | String | One (mandatory) |
| `images.caption` | A short caption for the image. | String | Zero-to-one |
| `images.contentUrl` | The URL where the image can be accessed. | String | Zero-to-one |
| `metadata` | Additional Metadata describing the thing. | [Dataset](https://schema.org/Dataset)-Object | Zero-to-one |
| `metadata["jsonld.type"]` | The type of the object, in this case 'Dataset'. | String | One (mandatory) |
| `metadata.encodingType` | The encoding type of the dataset. Must be one of `application/pdf`, `http://www.opengis.net/doc/IS/SensorML/2.0`,  `text/html` | String | Zero-to-one |
| `metadata.distribution` | Information about the dataset's distribution. Use this, if a download link is provided. | [DataDownload](https://schema.org/DataDownload)-Object | Zero-to-one |
| `metadata.distribution["jsonld.type"]` | The type of the object, in this case 'DataDownload'. | String | One (mandatory) |
| `metadata.distribution.url` | The URL to download the dataset. | String | Zero-to-one |
| `metadata.text` | Text representation of the metadata. Use this, if a SensorML or plain text representation should be provided. | String | Zero-to-one |
| `sourceRelatedThings` | A list of related things from which this object originates. | Array of Objects | Zero-to-many |
| `sourceRelatedThings["jsonld.id"]` | Unique ID of the related thing (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `sourceRelatedThings["jsonld.type"]` | The type of the object, in this case 'RelatedThing'. | String | One (mandatory) |
| `sourceRelatedThings.relationRole` | The role the object plays in the relationship. | Object | Zero-to-one |
| `sourceRelatedThings.relationRole["jsonld.type"]` | The type of the object, in this case 'RelationRole'. | String | One (mandatory) |
| `sourceRelatedThings.relationRole.name` | The name of the relationship (e.g., 'containedInPlace'). | String | Zero-to-one |
| `sourceRelatedThings.relationRole.definition` | URL to the definition of the relationship. | String | Zero-to-one |
| `sourceRelatedThings.relationRole.inverseName` | The name of the inverse relationship. | String | Zero-to-one |
| `sourceRelatedThings.relationRole.inverseDefinition` | URL to the definition of the inverse relationship. | String | Zero-to-one |
```

*Example*: Additional information for a *Thing*, in this case a climate station.

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
          "jsonld.id": "https://sensors.gfz.de/contacts/12345",
          "jsonld.type": "Person",
          "givenName": "John",
          "familyName": "Doe",
          "email": "john.doe@example.org",
          "affiliation": {
            "jsonld.type": "Organization",
            "name": "GFZ Helmholtz Centre for Geosciences",
            "identifier": "https://ror.org/04z8jg394"
          },
          "identifier": "https://orcid.org/0000-0000-0000-1234"
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

## *Sensor* properties

The `SensorProperties` schema definition serves as a structured extension for
the OGC SensorThings API (STA) `Sensor` entity. This schema definition allows for
the detailed documentation of sensors, including their unique identifiers, the
product group they belong to, whether they are virtual or physical, their
specific model and manufacturer details, serial numbers, and importantly,
information about the responsible persons, complete with their roles,
affiliations, and contact information.

```{table} Table 2: The Sensor properties
:name: tbl-sensor-properties
:class: thing-table
:align: left

| *Name* | Description | Datatype | Multiplicity |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used. | String | One (mandatory) |
| `jsonld.id` | Unique ID of the sensor (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `jsonld.type` | The type of the object, in this case 'SensorProperties'. | String | One (mandatory) |
| `identifier` | Another unique identifier for the object, e.g., a PID. | String | Zero-to-one |
| `isVariantOf` | Describes the product group the sensor belongs to. | [ProductGroup](https://schema.org/ProductGroup)-Object | Zero-to-one |
| `isVariantOf["jsonld.type"]` | The type of the object, in this case 'ProductGroup'. | String | One (mandatory) |
| `isVariantOf.name` | The name of the product group. | String | Zero-to-one |
| `isVariantOf.definition` | URL to the definition of the product group. | String | Zero-to-one |
| `isVirtual` | Indicates if the sensor is virtual. | Boolean | Zero-to-one |
| `model` | The model name of the sensor. | String | Zero-to-one |
| `manufacturer` | Information about the manufacturer of the sensor. | [Organization](https://schema.org/Organization)-Object | Zero-to-one |
| `manufacturer["jsonld.type"]` | The type of the object, in this case 'Organization'. | String | One (mandatory) |
| `manufacturer.name` | The name of the manufacturer. | String | Zero-to-one |
| `manufacturer.definition` | URL to the definition of the manufacturer. | String | Zero-to-one |
| `serialNumber` | The serial number of the sensor. | String | Zero-to-one |
| `responsiblePersons` | A list of persons responsible for the object. | Array of [Role](https://schema.org/Role)-Objects | Zero-to-many |
| `responsiblePersons["jsonld.type"]` | The type of the object, in this case 'Role'. | String | One (mandatory) |
| `responsiblePersons.roleName` | The name of the role (e.g., 'Owner'). | String | Zero-to-one |
| `responsiblePersons.definition` | URL to the definition of the role. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons` | A nested list of person objects fulfilling the role. | Array of [Person](https://schema.org/Person)-Objects | Zero-to-many |
| `responsiblePersons.responsiblePersons["jsonld.id"]` | Unique ID of the person (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `responsiblePersons.responsiblePersons["jsonld.type"]` | The type of the object, in this case 'Person'. | String | One (mandatory) |
| `responsiblePersons.responsiblePersons.givenName` | The person's given name. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.familyName` | The person's family name. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.email` | The person's email address. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation` | The organization the person is affiliated with. | [Organization](https://schema.org/Organization)-Object | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation["jsonld.type"]` | The type of the object, in this case 'Organization'. | String | One (mandatory) |
| `responsiblePersons.responsiblePersons.affiliation.name` | The name of the organization. | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.affiliation.identifier` | A unique identifier for the organization (e.g., ROR). | String | Zero-to-one |
| `responsiblePersons.responsiblePersons.identifier` | A unique identifier for the person (e.g., ORCID). | String | Zero-to-one |
```

*Example*: Additional information for a *Sensor*, in this case a Pressure Transducer.

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "jsonld.id": "https://sensors.gfz.de/devices/786",
  "jsonld.type": "SensorProperties",
  "identifier": "https://handle.net/1234567",
  "isVariantOf": {
    "jsonld.type": "ProductGroup",
    "name": "Pressure transducer",
    "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/equipmenttypes/42"
  },
  "isVirtual": false,
  "model": "AdconBP1",
  "manufacturer": {
    "jsonld.type": "Organization",
    "name": "OTT HydroMet",
    "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/manufacturers/48"
  },
  "serialNumber": "12345",
  "responsiblePersons": [
    {
      "jsonld.type": "Role",
      "roleName": "Owner",
      "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/contactroles/4",
      "responsiblePersons": [
        {
          "jsonld.id": "https://sensors.gfz.de/contacts/12345",
          "jsonld.type": "Person",
          "givenName": "Jane",
          "familyName": "Doe",
          "email": "jane.doe@example.org",
          "affiliation": {
            "jsonld.type": "Organization",
            "name": "GFZ Helmholtz Centre for Geosciences",
            "identifier": "https://ror.org/04z8jg394"
          },
          "identifier": ""
        }
      ]
    }
  ]
}
```

## *Datastream* properties 

The `DatastreamProperties` schema definition serves as a structured extension
for the OGC SensorThings API (STA) `Datastream` entity. It allows for a more
comprehensive description of a datastream by providing details about its
observing procedure, including specific parameters like the aggregation period
and its unit, as well as defining the measurement properties such as
resolution, accuracy, and operational range, complete with their respective
units. Furthermore, this schema accommodates information regarding the license
under which the data is provided, the mobility, specific deployment details
including timestamps and spatial offsets, and the data source from which the
datastream originates. 

```{table} Table 3: The Datastream properties
:name: tbl-datastream-properties
:class: thing-table
:align: left

| *Name* | Definition | Data type | Multiplicity and use |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | String/Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used (schema.org). | String | One (mandatory) |
| `jsonld.id` | Unique ID of the datastream (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `jsonld.type` | The type of the object, in this case 'DatastreamProperties'. | String | One (mandatory) |
| `observingProcedure` | Details about the observing procedure. | Object | Zero-to-one |
| `observingProcedure["jsonld.type"]` | The type of the object, in this case 'ObservingProcedure'. | String | One (mandatory) |
| `observingProcedure.name` | The name of the procedure. | String | Zero-to-one |
| `observingProcedure.description` | A description of the procedure. | String | Zero-to-one |
| `observingProcedure.definition` | URL to the definition of the procedure. | String | Zero-to-one |
| `observingProcedure.properties` | Additional properties of the procedure. | Object | Zero-to-one |
| `observingProcedure.properties.period` | The duration of the observation period. | Number | Zero-to-one |
| `observingProcedure.properties.unitOfPeriod` | The unit for the observation period. | Object | Zero-to-one |
| `observingProcedure.properties.unitOfPeriod["jsonld.type"]` | The type of the object, in this case 'Unit'. | String | One (mandatory) |
| `observingProcedure.properties.unitOfPeriod.name` | The name of the unit. | String | Zero-to-one |
| `observingProcedure.properties.unitOfPeriod.symbol` | The symbol for the unit. | String | Zero-to-one |
| `observingProcedure.properties.unitOfPeriod.definition` | URL to the definition of the unit. | String | Zero-to-one |
| `measurementProperties` | Properties of the measurement itself. | Object | Zero-to-one |
| `measurementProperties["jsonld.type"]` | The type of the object, in this case 'MeasurementProperties'. | String | One (mandatory) |
| `measurementProperties.measurementResolution` | The resolution of the measurement. | Number | Zero-to-one |
| `measurementProperties.unitOfMeasurementResolution` | The unit for the measurement resolution. | Object | Zero-to-one |
| `measurementProperties.unitOfMeasurementResolution["jsonld.type"]` | The type of the object, in this case 'Unit'. | String | One (mandatory) |
| `measurementProperties.unitOfMeasurementResolution.name` | The name of the unit. | String | Zero-to-one |
| `measurementProperties.unitOfMeasurementResolution.symbol` | The symbol for the unit. | String | Zero-to-one |
| `measurementProperties.unitOfMeasurementResolution.definition` | URL to the definition of the unit. | String | Zero-to-one |
| `measurementProperties.measurementAccuracy` | The accuracy of the measurement. | Number | Zero-to-one |
| `measurementProperties.unitOfMeasurementAccuracy` | The unit for the measurement accuracy. | Object | Zero-to-one |
| `measurementProperties.unitOfMeasurementAccuracy["jsonld.type"]` | The type of the object, in this case 'Unit'. | String | One (mandatory) |
| `measurementProperties.unitOfMeasurementAccuracy.name` | The name of the unit. | String | Zero-to-one |
| `measurementProperties.unitOfMeasurementAccuracy.symbol` | The symbol for the unit. | String | Zero-to-one |
| `measurementProperties.unitOfMeasurementAccuracy.definition` | URL to the definition of the unit. | String | Zero-to-one |
| `measurementProperties.operationRange` | The operational range of the measurement. | Array of Numbers | Zero-to-one |
| `measurementProperties.unitOfOperationRange` | The unit for the operational range. | Object | Zero-to-one |
| `measurementProperties.unitOfOperationRange["jsonld.type"]` | The type of the object, in this case 'Unit'. | String | One (mandatory) |
| `measurementProperties.unitOfOperationRange.name` | The name of the unit. | String | Zero-to-one |
| `measurementProperties.unitOfOperationRange.symbol` | The symbol for the unit. | String | Zero-to-one |
| `measurementProperties.unitOfOperationRange.definition` | URL to the definition of the unit. | String | Zero-to-one |
| `license` | Information about the license for the data. | [CreativeWork](https://schema.org/CreativeWork)-Object | Zero-to-one |
| `license["jsonld.type"]` | The type of the object, in this case 'CreativeWork'. | String | One (mandatory) |
| `license.name` | The name of the license. | String | Zero-to-one |
| `license.url` | The URL to the full license text. | String | Zero-to-one |
| `license.provider` | The provider of the license. | String | Zero-to-one |
| `providerMobility` | The mobility of the data provider (e.g., 'static'). | String | Zero-to-one |
| `deployment` | Details about the deployment of the datastream. | Object | Zero-to-one |
| `deployment["jsonld.id"]` | Unique ID of the deployment (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `deployment["jsonld.type"]` | The type of the object, in this case 'Deployment'. | String | One (mandatory) |
| `deployment.deploymentTime` | The time of deployment. | String | Zero-to-one |
| `deployment.properties` | Additional properties of the deployment. | Object | Zero-to-one |
| `deployment.properties["jsonld.type"]` | The type of the object, in this case 'DeploymentProperties'. | String | One (mandatory) |
| `deployment.properties.offsets` | The offsets of the deployment. | Object | Zero-to-one |
| `deployment.properties.offsets["jsonld.type"]` | The type of the object, in this case 'Offset'. | String | One (mandatory) |
| `deployment.properties.offsets.x` | The x-offset. | Number | Zero-to-one |
| `deployment.properties.offsets.y` | The y-offset. | Number | Zero-to-one |
| `deployment.properties.offsets.z` | The z-offset. | Number | Zero-to-one |
| `deployment.properties.unitOfOffsets` | The unit for the offsets. | Object | Zero-to-one |
| `deployment.properties.unitOfOffsets["jsonld.type"]` | The type of the object, in this case 'Unit'. | String | One (mandatory) |
| `deployment.properties.unitOfOffsets.name` | The name of the unit. | String | Zero-to-one |
| `deployment.properties.unitOfOffsets.symbol` | The symbol for the unit. | String | Zero-to-one |
| `deployment.properties.unitOfOffsets.definition` | URL to the definition of the unit. | String | Zero-to-one |
| `dataSource` | A descriptive string indicating the source of the data. | String | Zero-to-one |
```

*Example*: Additional information for a *Datastream*

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "jsonld.id": "https://sensors.gfz.de/datastream-links/6",
  "jsonld.type": "DatastreamProperties",
  "observingProcedure": {
    "jsonld.type": "ObservingProcedure",
    "name": "mean",
    "description": "the arithmetic mean value",
    "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/aggregationtypes/1",
    "properties": {
      "period": 600,
      "unitOfPeriod": {
        "jsonld.type": "Unit",
        "name": "seconds",
        "symbol": "s",
        "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/units/63"
      }
    }
  },
  "measurementProperties": {
    "jsonld.type": "MeasurementProperties",
    "measurementResolution": 0.2,
    "unitOfMeasurementResolution": {
      "jsonld.type": "Unit",
      "name": "seconds",
      "symbol": "sec",
      "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/units/58"
    },
    "measurementAccuracy": 1.0,
    "unitOfMeasurementAccuracy": {
      "jsonld.type": "Unit",
      "name": "millibars",
      "symbol": "mbar",
      "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/units/64"
    },
    "operationRange": [
      500.0,
      1500.0
    ],
    "unitOfOperationRange": {
      "jsonld.type": "Unit",
      "name": "millibars",
      "symbol": "mbar",
      "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/units/64"
    }
  },
  "license": {
    "jsonld.type": "CreativeWork",
    "name": "GPLv3",
    "url": "https://www.gnu.org/licenses/gpl-3.0.txt",
    "provider": "The HMC-STAMPLATE project consortium"
  },
  "providerMobility": "static",
  "deployment": {
    "jsonld.id": "https://sensors.gfz.de/configurations/35/platforms-and-devices?deviceMountAction=182",
    "jsonld.type": "Deployment",
    "deploymentTime": "2020-01-01T00:50-03:00",
    "properties": {
      "jsonld.type": "DeploymentProperties",
      "offsets": {
        "jsonld.type": "Offset",
        "x": -3,
        "y": 2,
        "z": 10
      },
      "unitOfOffsets": {
        "jsonld.type": "Unit",
        "name": "meters",
        "symbol": "m",
        "definition": "https://sms-cv.helmholtz.cloud/sms/cv/api/v1/units/63"
      }
    }
  },
  "dataSource": "ftp/uploads01"
}
```

## *Location* properties

The `LocationProperties` schema definition serves as a structured extension for
the OGC SensorThings API (STA) `Location` entity.

No specific properties have been defined so far.

```{table} Table 4: The Location properties
:name: tbl-location-properties
:class: thing-table
:align: left

| *Name* | Definition | Data type | Multiplicity and use |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | String/Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used (schema.org). | String | One (mandatory) |
| `jsonld.id` | Unique ID of the location (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `jsonld.type` | The type of the object, in this case 'LocationProperties'. | String | One (mandatory) |
```

*Example*: Additional information for a *Location*

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "jsonld.id": "https://sensors.gfz.de/configurations/35/locations/static-location-actions/15",
  "jsonld.type": "LocationProperties"
}
```

## *ObservedProperty* properties

The `ObservedPropertyProperties` schema definition serves as a structured
extension for the OGC SensorThings API (STA) `ObservedProperty` entity.

No specific properties have been defined so far.

```{table} Table 5: The Observed Property properties
:name: tbl-property-properties
:class: thing-table
:align: left

| *Name* | Definition | Data type | Multiplicity and use |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | String/Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used (schema.org). | String | One (mandatory) |
| `jsonld.id` | Unique ID of the Observed Property (e.g., the URL to its representation in an application). | String | One (mandatory) |
| `jsonld.type` | The type of the object, in this case 'ObservedPropertyProperties'. | String | One (mandatory) |
```

*Example*: Additional information for an *ObservedProperty*

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "jsonld.id": "https://sensors.gfz.de/cv/api/v1/measuredquantities/32/",
  "jsonld.type": "ObservedPropertyProperties"
}
```

## *Observation* properties

The `ObservationProperties` schema definition serves as a structured extension
for the OGC SensorThings API (STA) `Observation` entity.

```{table} Table 6: The Observation properties
:name: tbl-observation-properties
:class: thing-table
:align: left

| *Name* | Definition | Data type | Multiplicity and use |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | String/Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used (schema.org). | String | One (mandatory) |
| `jsonld.type` | The type of the object, in this case 'ObservationProperties'. | String | One (mandatory) |
| `dataSource` | A descriptive string indicating the source of the observation data. | String | Zero-to-one |
```

*Example*: Additional information for an *Observation*

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "jsonld.type": "ObservationProperties",
  "dataSource": "file01.csv"
}
```

## *Observation ResultQuality* properties

> [!WARNING]
> Work in progress

```{table} Table 7: The Observation Result Quality properties
:name: tbl-observation-resultquality-properties
:class: thing-table
:align: left

| *Name* | Definition | Data type | Multiplicity and use |
| :--- | :--- | :--- | :--- |
| `@context` | JSON-LD context for defining keywords and vocabulary. | Object | One (mandatory) |
| `@context.@version` | The version of the context. | String/Number | One (mandatory) |
| `@context.@import` | Import URL for the STAMPLATE context. | String | One (mandatory) |
| `@context.@vocab` | The default vocabulary used (schema.org). | String | One (mandatory) |
| `annotations` | A list of annotations for the object. | Array of Objects | Zero-to-many |
| `annotations.@id` | Unique ID of the annotation. | String | Zero-to-one |
| `annotations.@type` | The type of the annotation, in this case 'ObservationResultQuality'. | String | One (mandatory) |
| `annotations.annotation` | The value of the annotation. | String | Zero-to-one |
| `annotations.annotationType` | The type of the annotation (e.g., 'SaQC', 'generic'). | String | Zero-to-one |
| `annotations.properties` | Additional properties of the annotation. | Object | Zero-to-one |
| `annotations.properties.version` | The version of the annotation. | String | Zero-to-one |
| `annotations.properties.measure` | The measure used for the annotation. | String | Zero-to-one |
| `annotations.properties.definition` | URL to the definition of measure. | String | Zero-to-one |
```

*Example*: Additional information for the *ResultQuality*

```JSON
{
  "@context": {
    "@version": 1.1,
    "@import": "stamplate.jsonld",
    "@vocab": "http://schema.org/"
  },
  "annotations": [
    {
      "@id": "https://rdm-software.pages.ufz.de/saqc/",
      "@type": "ObservationResultQuality",
      "annotation": "99",
      "annotationType": "SaQC",
      "properties": {
        "version": "2.6",
        "measure": "flagUniLOF",
        "definition": "https://url/to/config"
      }
    },
    {
      "@id": "https://tereno.net/quality",
      "@type": "ObservationResultQuality",
      "annotation": "baddata",
      "annotationType": "generic"
    },
    {
      "@id": "https://tereno.net/quality",
      "@type": "ObservationResultQuality",
      "annotation": "Analysis error",
      "annotationType": "specific"
    }
  ]
}
```

