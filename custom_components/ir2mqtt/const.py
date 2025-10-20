
DOMAIN = "ir2mqtt"
DEFAULT_TOPIC_PREFIX = "iracing"

DEVICE_INFO = {
    "name": "iRacing Telemetry",
    "manufacturer": "iR2mqtt",
    "model": "iR2mqtt Data Feed",
    "sw_version": "1.3.3",
}

SENSOR_DEFINITIONS = {
    "speed_ms": {
        "name": "Speed m/s",
        "value_template": "{{ value_json.speed | float(0) | round(1) }}",
        "unit_of_measurement": "m/s",
        "device_class": "speed",
        "icon": "mdi:speedometer",
    },
    "speed_kmh": {
        "name": "Speed km/h",
        "value_template": "{{ (value_json.speed | float(0) * 3.6) | round(1) }}",
        "unit_of_measurement": "km/h",
        "device_class": "speed",
        "icon": "mdi:speedometer",
    },
    "speed_mph": {
        "name": "Speed mph",
        "value_template": "{{ (value_json.speed | float(0) * 2.237) | round(1) }}",
        "unit_of_measurement": "mph",
        "device_class": "speed",
        "icon": "mdi:speedometer",
    },
    "rpm": {
        "name": "RPM",
        "value_template": "{{ value_json.rpm | int(0) }}",
        "unit_of_measurement": "RPM",
        "icon": "mdi:engine",
    },
    "gear": {
        "name": "Gear",
        "value_template": "{{ value_json.gear }}",
        "icon": "mdi:car-shift-pattern",
    },
    "fuel_level": {
        "name": "Fuel Level",
        "value_template": "{{ value_json.fuel_level | float(0) | round(2) }}",
        "unit_of_measurement": "L",
        "icon": "mdi:gas-station",
    },
    "lap": {
        "name": "Lap",
        "value_template": "{{ value_json.lap | int(0) }}",
        "unit_of_measurement": "lap",
        "icon": "mdi:flag-checkered",
    },
    "session_time": {
        "name": "Session Time",
        "value_template": "{{ (value_json.session_time | float(0) / 60) | round(2) }}",
        "unit_of_measurement": "min",
        "device_class": "duration",
        "icon": "mdi:clock",
    },
    "time_remaining": {
        "name": "Time Remaining",
        "value_template": "{{ (value_json.session_time_remain | float(0) / 60) | round(2) }}",
        "unit_of_measurement": "min",
        "device_class": "duration",
        "icon": "mdi:clock-end",
    },
    "session_type": {
        "name": "Session Type",
        "value_template": "{{ value_json.session_type }}",
        "icon": "mdi:trophy",
    },
    "session_name": {
        "name": "Session Name",
        "value_template": "{{ value_json.session_name }}",
        "icon": "mdi:format-title",
    },
    "active_flag": {
        "name": "Active Flag",
        "value_template": "{{ value_json.active_flags[0] if value_json.active_flags else 'No Flag' }}",
        "icon": "mdi:flag",
        "json_attributes_template": "{ \"all_flags\": {{ value_json.active_flags | tojson }}, \"session_flags\": {{ value_json.session_flags }} }",
    },
    "timestamp": {
        "name": "Timestamp",
        "value_template": "{{ value_json.timestamp }}",
        "icon": "mdi:clock-digital",
    },
    "incidents": {
        "name": "Incidents",
        "value_template": "{{ value_json.incs }}",
        "icon": "mdi:alert",
    },
    "start_lights": {
        "name": "Start Lights",
        "value_template": "{{ value_json.active_lights[0] if value_json.active_lights else 'No Lights' }}",
        "icon": "mdi:traffic-light",
        "json_attributes_template": "{ \"all_lights\": {{ value_json.active_lights | tojson }} }",
    },
}

BINARY_SENSOR_DEFINITIONS = {
    "on_pit_road": {
        "name": "On Pit Road",
        "value_template": "{{ value_json.get('on_pit_road', False) }}",
        "icon": "mdi:gauge",
    },
    
    "flag_checkered": {
        "name": "Checkered Flag",
        "value_template": "{{ 'Checkered' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag-checkered",
    },
    "flag_white": {
        "name": "White Flag",
        "value_template": "{{ 'White' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag-outline",
    },
    "flag_green": {
        "name": "Green Flag",
        "value_template": "{{ 'Green' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag-variant",
    },
    "flag_yellow": {
        "name": "Yellow Flag",
        "value_template": "{{ 'Yellow' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_red": {
        "name": "Red Flag",
        "value_template": "{{ 'Red' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_blue": {
        "name": "Blue Flag",
        "value_template": "{{ 'Blue' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_debris": {
        "name": "Debris Flag",
        "value_template": "{{ 'Debris' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_crossed": {
        "name": "Crossed Flag",
        "value_template": "{{ 'Crossed' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_yellow_waving": {
        "name": "Yellow Waving Flag",
        "value_template": "{{ 'Yellow Waving' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_black": {
        "name": "Black Flag",
        "value_template": "{{ 'Black' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_repair": {
        "name": "Repair Flag",
        "value_template": "{{ 'Repair' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_caution": {
        "name": "Caution Flag",
        "value_template": "{{ 'Caution' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_caution_waving": {
        "name": "Caution Waving Flag",
        "value_template": "{{ 'Caution Waving' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_disqualify": {
        "name": "Disqualify Flag",
        "value_template": "{{ 'Disqualify' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_furled": {
        "name": "Furled Flag",
        "value_template": "{{ 'Furled' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_green_held": {
        "name": "Green Held Flag",
        "value_template": "{{ 'Green Held' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },
    "flag_random_waving": {
        "name": "Random Waving Flag",
        "value_template": "{{ 'Random Waving' in value_json.get('active_flags', []) }}",
        "icon": "mdi:flag",
    },

    "light_ready": {
        "name": "Ready Light",
        "value_template": "{{ 'Ready' in value_json.get('active_lights', []) }}",
        "icon": "mdi:traffic-light",
    },
    "light_set": {
        "name": "Set Light",
        "value_template": "{{ 'Set' in value_json.get('active_lights', []) }}",
        "icon": "mdi:traffic-light",
    },
    "light_go": {
        "name": "Go Light",
        "value_template": "{{ 'Go' in value_json.get('active_lights', []) }}",
        "icon": "mdi:traffic-light",
    },
}
