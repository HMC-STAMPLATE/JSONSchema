# Thing-properties

[`Thing.properties`](https://codebase.helmholtz.cloud/stamplate/jsonschemas/-/blob/main/schemas/thing_properties.schema.json)

| *Property*            | O2A Registry                                                        | SMS                                                 |
|-----------------------|---------------------------------------------------------------------|-----------------------------------------------------|
| `@id`                 | `{O2A-Registry}/items/{item.@uuid}`                      | `{SMS}/configurations/{configuration_id}`                                                   |
| `partOfProjects`      | candidate: `item.collections`                                                                    | `configuration.project`                             |
| `identifier`          | `item.@uuid`                                                        | `configuration.persistent_identifier`               |
| `metadata`            | `{O2A-Registry}/rest/v2/items/%7bitem.id%7d?with=all` | `{SMS}/backend/api/v1/devices/{device_id}/sensorml` |
| `sourceRelatedThings` | TBD, `item.parentId`?                                                                   | `configuration.site`                                |
| `responsiblePersons`  | `item.contacts`                                                     | `configuration_contact_role.contact`      
