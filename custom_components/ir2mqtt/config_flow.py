import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from homeassistant.core import callback

from .const import DOMAIN, DEFAULT_TOPIC_PREFIX

CONF_TOPIC_PREFIX = "topic_prefix"


class Ir2mqttConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(title="iR2mqtt", data=user_input)

        data_schema = vol.Schema(
            {
                vol.Optional(
                    CONF_TOPIC_PREFIX, default=DEFAULT_TOPIC_PREFIX
                ): str,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
