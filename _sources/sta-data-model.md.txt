# The OGC SensorThings API

The SensorThings API (STA) is a dedicated Open Geospatial Consortium (OGC) standard for making data from IoT-systems available over the web. Version 1.0 was released in 2016 and described the Sensing part {cite}`sta_1.0`. This was extended by a Tasking part in 2019  {cite}`sta_1.0_tasking`. Currently, STA is available in version 1.1 {cite}`sta_1.1` while a release of the next version 2.0 is planned for late 2025.

The *core* of STA consists of a lightweight and generic data model as well as an API that follows the REST-principles. As STA is tailored towards ressource-constrained IoT-appilcations, it also features efficient JSON encoding as well as the usage of MQTT- and OASIS OData protocols. 

![STA Data Model](_static/images/sta_data_model.png)