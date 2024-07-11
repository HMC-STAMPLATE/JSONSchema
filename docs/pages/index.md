---
layout: base.md
title: HMC STAMPLATE JSON Schema Definitions
date: Last Modified
---

# {{ title }}

## JSON Schemas

{% for schema in schemaFiles %}
- [{{ schema }}](/{{ CI_PROJECT_NAME }}/schemas/{{ schema }})
{% endfor %}

## JSON-LD Context

- [stamplate.jsonld](/{{ CI_PROJECT_NAME }}/vocab/stamplate.jsonld)
