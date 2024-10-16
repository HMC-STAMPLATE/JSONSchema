---
opengraph:
  title: STA JSON SCHEMA MAPPING DOCUMENTATION
  description: Draft for the document https://codebase.helmholtz.cloud/stamplate/jsonschemas/documentation/mapping.md
  tags: STAMPLATE, STA, JSONSCHEMA
  link to the draft: https://notes.desy.de/4GayFX1ZQiGrIqkzPQbgOQ
---

# STA Properties Mappings

This document serves as an additional documentation of concrete use cases for the HMC-STAMPLATE JSON schemas and an implementation of mappings between existing metadata management systems and the STA data model.

Originally, the JSON schemas are based on the requirements of the two sensor-metadata systems [O2A Registry](https://registry.o2a-data.de/) and [Sensor Management System (SMS)](https://helmholtz.software/software/sensor-management-system). The mappings from theses source system fields to the corresponding STA-properties fields are given below.

To increase readability, the constant fields `@type` are not shown here. The descriptions of the field semantics are given as links behind the fields. You can find all the details in the schema definitions.

## [`Thing.properties`](https://codebase.helmholtz.cloud/stamplate/jsonschemas/-/blob/main/schemas/thing_properties.schema.json)

| *Property*            | O2A Registry                                                        | SMS                                                 |
|-----------------------|---------------------------------------------------------------------|-----------------------------------------------------|
| `@id`                 | `{O2A-Registry}/items/{item.@uuid}`                      | `{SMS}/configurations/{configuration_id}`                                                   |
| `partOfProjects`      | candidate: `item.collections`                                                                    | `configuration.project`                             |
| `identifier`          | `item.@uuid`                                                        | `configuration.persistent_identifier`               |
| `metadata`            | `{O2A-Registry}/rest/v2/items/%7bitem.id%7d?with=all` | `{SMS}/backend/api/v1/devices/{device_id}/sensorml` |
| `sourceRelatedThings` | TBD, `item.parentId`?                                                                   | `configuration.site`                                |
| `responsiblePersons`  | `item.contacts`                                                     | `configuration_contact_role.contact`                |



## [`Sensor.properties`](https://codebase.helmholtz.cloud/stamplate/jsonschemas/-/blob/main/schemas/sensor_properties.schema.json)

| *Property*           | O2A Registry                                   | SMS                                          |
|----------------------|------------------------------------------------|----------------------------------------------|
| `@id`                | `{O2A-Registry}/items/{item.@uuid}` | `{SMS}/devices/{device_id}`                  |
| `isVariantOf`        | `item.type.generalName`                        | `device.device_type_name`                    |
| `manufacturer`       | `item.manufacturer`                            | `device.manufacturer_name`                   |
| `model`              | `item.model`                                   | `device.model`                               |
| `serialNumber`       | `item.serial_number`                           | `device.serialNumber`                        |
| `responsiblePersons` | `item.contacts`                                | `configuration_contact_role.contact`         |
| `identifier`         | `item.@uuid`                                              | `device.persistent_identifier`               |
| `isVirtual`          | *NA*                                              | `false` (only `true` for `{SMS}/procedures`) |


## [`Datastream.properties`](https://codebase.helmholtz.cloud/stamplate/jsonschemas/-/blob/main/schemas/datastream_properties.schema.json)

| *Property*                 | O2A Registry                                                                      | SMS                                                                                                                                              | Remarks      |
|----------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| `@id`                      | `{O2A-Registry}/rest/v2/items/{item_id}/parameters/{paramerter_id}` | `{SMS}/datastream-links/{datastream_link_id}`                                                                                                    |              |
| `observingProcedure`       | *NA*                                                                                 | `{SMS}/device-properties/{device-property_id}/aggregation_type_name` joint with `{SMS}/datastream-links/{datastream_link_id}/aggregation_period` |              |
| `measurementProperties`    | `parameters.properties`                                                           | `device_property.{resolution\|resolution_unit\|accuracy\|measuring_range_min\|measuring_range_max}`                                              | All supported keys are available at `{O2A-Registry}/rest/v2/vocables?where=vocableGroup.id==9` |
| `license`                  | filled by ingest, should default to `CC BY 4.0`                                                                                 | `{SMS}/datastream-links/{datastream_link_id}/license_{name\|uri}`                                                                                |              |
| `providerMobility`         | filled by ingest                                                                                   | derived from `static_location_action` and/or `dynamic_location_action`                                                                           |              |
| `deployment`               | `{O2A-Registry}/rest/v2/items/{item.id}/events?where=type.uuid%3D%3D047a4f46-020b-4187-808a-6f245caebbc3`                                                                                  | `{SMS}/configurations/{configuration_id}/platforms-and-devices?deviceMountAction={device_mount_action_id}`                                       |              |
| `sourceRelatedDatastreams` | *NA*                                                                                 | related datastreams continuing or compiling this one                                                                                             |              |
| `dataSource`               |                                                                                   |                                                                                                                                                  | filled by TSM |


## [`ObservedProperty.properties`](https://codebase.helmholtz.cloud/stamplate/jsonschemas/-/blob/main/schemas/observed_property_properties.schema.json)

| *Property* | O2A Registry                                                 | SMS                                                                                     |
|------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `@id`      | `{O2A-Registry}/rest/v2/vocables/{vocable_id}` | `https://sms-cv.helmholtz.cloud/sms/cv/api/v1/measuredquantities/{measuredquantity_id}` |


## [`Location.properties`](https://codebase.helmholtz.cloud/stamplate/jsonschemas/-/blob/main/schemas/location_properties.schema.json)

| *Property* | O2A Registry | SMS                                                                                                     |
|------------|--------------|---------------------------------------------------------------------------------------------------------|
| `@id`      | ? probably *NA*            | `{SMS}/configurations/{configuration_id}/locations/static-location-actions/{static_location_action_id}` |


## [`Observation.properties`](https://codebase.helmholtz.cloud/stamplate/jsonschemas/-/blob/main/schemas/observation_properties.schema.json)

| *Property*   | O2A Registry | SMS | Remarks       |
|--------------|--------------|-----|---------------|
| `@id`        | ?            | ?   |               |
| `dataSource` | filled by ingest |     | filled by TSM |


