# {{ project_title }} 

**Authors:** {{ project_authors }}

**DOI:** {% if project_doi %}[{{ project_doi }}](https://doi.org/{{ project_doi }}){% else %}_to be assigned_{% endif %}

Welcome! This site documents the JSON Schemas and guidance for using the `properties` objects of core **OGC SensorThings API (STA)** entities in the **STAMPLATE** context.

Small text...

```{toctree}
:caption: Contents
:maxdepth: 2

getting-started
sta-data-model
schemas/Thing

```

## Citing

If you use this profile, please cite the corresponding Zenodo record.

## References

```{bibliography}
:cited:
:style: unsrt