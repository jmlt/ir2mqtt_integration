import json
import logging

from homeassistant.components import mqtt
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.json import JSONEncoder

from .const import (
    BINARY_SENSOR_DEFINITIONS,
    DEVICE_INFO,
    DOMAIN,
    SENSOR_DEFINITIONS,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    
    topic_prefix = entry.data.get("topic_prefix", "iracing")
    state_topic = f"{topic_prefix}/telemetry"

    device_registry = dr.async_get(hass)
    connection_id = f"ir2mqtt_{entry.entry_id}"

    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        connections={(dr.CONNECTION_NETWORK_MAC, connection_id)},
        name=DEVICE_INFO["name"],
        manufacturer=DEVICE_INFO["manufacturer"],
        model=DEVICE_INFO["model"],
        sw_version=DEVICE_INFO["sw_version"],
    )

    publisher = MqttPublisher(hass, entry, connection_id)
    hass.data[DOMAIN][entry.entry_id] = publisher
    await publisher.async_publish_discovery_configs(state_topic)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    publisher = hass.data[DOMAIN].pop(entry.entry_id)
    await publisher.async_remove_discovery_configs()
    
    return True


class MqttPublisher:

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, connection_id: str):
        self.hass = hass
        self.entry = entry
        self.connection_id = connection_id

    async def async_publish_discovery_configs(self, state_topic: str):
        _LOGGER.info("Publishing iR2mqtt discovery messages")
        for key, config in SENSOR_DEFINITIONS.items():
            await self._publish_entity_config(Platform.SENSOR, key, config, state_topic)

        for key, config in BINARY_SENSOR_DEFINITIONS.items():
            await self._publish_entity_config(Platform.BINARY_SENSOR, key, config, state_topic)

    async def async_remove_discovery_configs(self):
        _LOGGER.info("Removing iR2mqtt discovery messages")
        for key in SENSOR_DEFINITIONS:
            await self._remove_entity_config(Platform.SENSOR, key)

        for key in BINARY_SENSOR_DEFINITIONS:
            await self._remove_entity_config(Platform.BINARY_SENSOR, key)

    async def _publish_entity_config(self, platform: Platform, key: str, config: dict, state_topic: str):
        unique_id = f"ir2mqtt_{key}"
        discovery_topic = f"homeassistant/{platform}/{unique_id}/config"
        
        payload_config = config.copy()
        entity_name = payload_config.pop("name", key)

        device_payload = {
            "connections": [
                [dr.CONNECTION_NETWORK_MAC, self.connection_id]
            ],
            "name": DEVICE_INFO["name"],
            "manufacturer": DEVICE_INFO["manufacturer"],
            "model": DEVICE_INFO["model"],
            "sw_version": DEVICE_INFO["sw_version"],
        }
        
        payload = {
            **payload_config,
            "name": f"iR2mqtt {entity_name}",
            "unique_id": unique_id,
            "state_topic": state_topic,
            "device": device_payload,
            "expire_after": 30,
        }
        

        if "json_attributes_template" in payload:
            payload["json_attributes_topic"] = state_topic

        await mqtt.async_publish(
            self.hass,
            discovery_topic,
            json.dumps(payload, cls=JSONEncoder),
            retain=True,
            qos=0,
        )

    async def _remove_entity_config(self, platform: Platform, key: str):
        unique_id = f"ir2mqtt_{key}"
        discovery_topic = f"homeassistant/{platform}/{unique_id}/config"
        await mqtt.async_publish(
            self.hass, discovery_topic, "", retain=True, qos=0
        )