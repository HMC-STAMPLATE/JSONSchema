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

## `Thing.properties`

| *Property* | O2A Registry | SMS         |
|------------|--------------|-------------|
|`@id`                |`https://registry.o2a-data.de/items/{item.id}` |
|`partOfProjects`     | |
|`identifier`         | |
|`metadata`           | |
|`sourceRelatedThings`| |
|`responsiblePersons` | |



## `Sensor.properties`


| *Property* | O2A Registry | SMS         |
|------------|--------------|-------------|
| `@id`                | |
| `isVariantOf`        | |
| `manufacturer`       | |
| `model`              | |
| `serialNumber`       | |
| `responsiblePersons` | |
| `identifier`         | |
| `isVirtual`          | |


### `Datastream.properties`

| *Property* | O2A Registry | SMS         |
|------------|--------------|-------------|
| `@id`      | |
| `observingProcedure` | |
| `measurementProperties` | |
| `license`             | |
| `providerMobility`   | |
| `deployment`         | |
| `sourceRelatedDatastreams` | |
| `dataSource` | |


### `ObservedProperty.properties`

| *Property* | O2A Registry | SMS         |
|------------|--------------|-------------|
| `@id`      | |


### `Location.properties`

| *Property* | O2A Registry | SMS         |
|------------|--------------|-------------|
| `@id`      | |


### `Observation.properties`

| *Property* | O2A Registry | SMS         |
|------------|--------------|-------------|
| `@id`      | |
| `dataSource`  | |


