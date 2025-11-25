'''
OGC API records harvester for STA endpoints.

Using "@context": {
          "@vocab": "http://schema.org/",
          "@import": "stamplate.jsonld",
          "@version": 1.1
        }

@author u.loup@fz-juelich.de
'''
import argparse
import requests

STA_ENTITY_TYPES = ['Things', 'Datastreams', 'Sensors', 'ObservedProperties']

OGC_API_RECORD_TEMPLATE = {
    'id': "",
    'type': "",
    'title': "",
    'description': "",
    'geometry': "",
    'time': "",
    'assets': "",
    'keywords': "",
    'externalIds': "",
    'contacts': "",
    'license': "",
    "links": [
        {"rel": "alternate", "href": "https://sta.example.org/v1.1/Things(123)"},
        {"rel": "datastreams", "href": "https://sta.example.org/v1.1/Things(123)/Datastreams"},
        {"rel": "observedProperties", "href": "https://sta.example.org/v1.1/Things(123)/ObservedProperties"},
        {"rel": "sensors", "href": "https://sta.example.org/v1.1/Things(123)/Sensors"}
    ],
    'created': ""
}


def prepare_sta_call(url):
    '''Returns the entity type and the URL in the correct format for use with this script. If the URL does not point to a supported STA entity, None is returned.'''
    if url:
        if url.endswith("/"):
            url = url[:-1]
        for sta_entity_type in STA_ENTITY_TYPES:
            if url.endswith(sta_entity_type):
                params = {}
                if sta_entity_type == "Things":
                    params = {
                        '$select': '@iot.id,@iot.selfLink,name,description,properties',
                        '$expand': [
                            'Datastreams($select=@iot.id,@iot.selfLink,name,description,properties;$expand=Sensor($select=@iot.id,name,description,encodingType,metadata,properties);$expand=ObservedProperty($select=@iot.id,name,definition,description,properties))',
                            'Locations($select=location)',
                            'HistoricalLocations($select=time)']
                    }
                return sta_entity_type, url, params
    return None


def compute_bounding_box(sta_locations):
    """Computes bounding-box coordinates [longitude_min, latitude_min, longitude_max, latitude_max] from the given
    list of STA locations [ {"type": ..., "coordinates": ...} ]."""
    longitudes = []
    latitudes = []
    for location in sta_locations:
        if location['type'] == 'Point':
            longitudes.append(location['coordinates'][0])
            latitudes.append(location['coordinates'][1])
    if longitudes and latitudes:
        return [min(longitudes), min(latitudes), max(longitudes), max(latitudes)]
    return None


def compute_time_range(sta_times):
    """Computes a time range from the given list of ISO timestamps with historical locations."""
    if sta_times:
        if sta_times.__len__() > 1:
            return f"{min(sta_times)[:-1]}/{max(sta_times)[:-1]}S"
        return sta_times[0]
    return None


def get_contacts(sta_properties):
    if "responsiblePersons" in sta_properties:
        name_roles = {}
        for role in sta_properties["responsiblePersons"]:
            persons = role["responsiblePersons"]
            for person in persons:
                name = f"{person['givenName']} {person['familyName']}"
                if name in name_roles:
                    name_roles[name].append(role["roleName"])
                else:
                    name_roles[name] = [role["roleName"]]
        return [{name: name_roles[name]} for name in name_roles.keys()]
    return None


def get_entities(url, params={}):
    """Calls GET at the specified url with the given parameters and returns the list of entities if no error occurred."""
    assert isinstance(params, dict)
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1)
    session.mount('https://', adapter)
    # self.session.headers.update({'accept': 'application/vnd.api+json', 'X-APIKEY': apikey})
    while True:
        r = session.get(url, params=params)
        json = r.json()
        break
    session.close()
    return json["value"]


def create_thing_record(sta_thing):
    record = dict()
    record["id"] = sta_thing["@iot.selfLink"]
    record["type"] = "Thing"
    record["title"] = sta_thing["name"]
    record["description"] = sta_thing["description"]
    record["geometry"] = compute_bounding_box([location["location"] for location in sta_thing["Locations"]])
    record["time"] = compute_time_range(
        [historical_location['time'] for historical_location in sta_thing["HistoricalLocations"]])
    record["contacts"] = get_contacts(sta_thing["properties"])
    record["links"] = [{"rel": "collection", "href": datastream['@iot.selfLink']} for datastream in
                       sta_thing["Datastreams"]]
    return record


def create_datastreams_record(sta_entity):
    record = dict(OGC_API_RECORD_TEMPLATE)
    record["title"] = sta_entity["name"]
    return record


def create_sensors_record(sta_entity):
    record = dict(OGC_API_RECORD_TEMPLATE)
    record["title"] = sta_entity["name"]
    return record


def create_observed_properties_record(sta_entity):
    record = dict(OGC_API_RECORD_TEMPLATE)
    record["title"] = sta_entity["name"]
    return record


def parse_arguments():
    """Configures and executes the argument parser and returns the command-line arguments in a Namespace."""
    parser = argparse.ArgumentParser(
        description='Tool to map entities from SensorThings API (STA) endpoints to OGC API records.',
        prog='python sta_to_ogcapi-records.py',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('url',
                        help='URL to one or many STA entities')
    args = parser.parse_args()
    return args


def main():
    """Main method of the application"""
    args = parse_arguments()
    print(args)
    entity_type, url, params = prepare_sta_call(args.url)
    entities = get_entities(url, params)
    records = []
    for entity in entities:
        if entity_type == STA_ENTITY_TYPES[0]:
            records.append(create_thing_record(entity))
        elif entity_type == STA_ENTITY_TYPES[1]:
            records.append(create_datastreams_record(entity))
        elif entity_type == STA_ENTITY_TYPES[2]:
            records.append(create_sensors_record(entity))
        elif entity_type == STA_ENTITY_TYPES[3]:
            records.append(create_observed_properties_record(entity))
    for record in records:
        print(record)


if __name__ == '__main__':
    main()
