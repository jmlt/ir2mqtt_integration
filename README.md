# iR2mqtt – Home Assistant Integration

![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange)
![HACS Integration](https://img.shields.io/badge/HACS-Integration-blue)
![Release](https://img.shields.io/github/v/release/jmlt/ir2mqtt_integration)

Home Assistant integration for [iR2mqtt](https://github.com/jmlt/ir2mqtt). Automatically creates iRacing telemetry sensors from MQTT data.

---

## ✨ Features

* **Automatic Discovery:** Automatically creates and configures sensors and binary sensors related to iRacing telemetry.  
* **Unified Device:** All entities are grouped under a single “iRacing Telemetry” device for a clean, organized structure inside Home Assistant.  
* **Included Sensors:**
  * **Sensors:** Speed (m/s, km/h, mph), RPM, Gear, Fuel Level, Current Lap, Session Time, Session Type, Incidents, Start Lights, and more.
  * **Binary Sensors:** On Pit Road, Active Flags (Green, Yellow, White, Blue, etc.), Start Lights (Ready, Set, Go).

---

## 🧩 Requirements

To use this integration, you must have:

1. A configured **MQTT Broker**. The official [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) add-on is recommended.  
   Ensure the MQTT integration in Home Assistant is properly connected to your broker.  
2. **[iR2mqtt](https://github.com/jmlt/ir2mqtt)** and iRacing running to read iRacing telemetry.  

---

## 📦 Installation (via HACS)
 
1. **Add this repository as a Custom Repository** (until it’s officially listed in HACS):
   - Go to **HACS → Integrations**.
   - Click the three-dot menu (top right) → **Custom repositories**.
   - **Repository URL:** Paste the URL of this GitHub repository <pre>https://github.com/jmlt/ir2mqtt_integration/</pre>
   - **Category:** Select `Integration`.
   - Click **Add**.
2. Restart Home Assistant. 
3. Proceed to Configuration

<details>
<summary>Without HACS</summary>

1. Download the latest release of the iR2mqtt integration from [GitHub Releases)](https://github.com/jmlt/ir2mqtt_integration/releases).
2. Extract the downloaded files and place the ir2mqtt folder in your Home Assistant custom_components directory (usually located in the config/custom_components directory).
3. Restart your Home Assistant instance to load the new integration.
</details>

---

## ⚙️ Configuration

After installation and restarting Home Assistant, setup is done through the UI:

1. Go to **Settings → Devices & Services**.  
2. Click **Add Integration** and search for **iR2mqtt**.  
   Alternatively, you can click this button to start directly:  
   [![Add Integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ir2mqtt)
3. Enter the **MQTT Topic Prefix** (if you changed the default):
   * Default value: `iracing`.
4. Click **Submit**.

A new device called **iRacing Telemetry** will be created immediately.  
Entities will initially appear as “Unavailable”. They will automatically update and become active once iR2mqtt app starts publishing telemetry data.

Here is an [automation](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/automation-example.yaml) example that controls light entity according to iracing flags.

---

## Home Assistant Community Post
https://community.home-assistant.io/t/ir2mqtt-bring-iracing-live-telemetry-to-home-assistant/901589

---
## ⚠️ Disclaimer

This project is an **unofficial community integration** and is **not affiliated, associated, authorized, endorsed by, or in any way officially connected with**  
**iRacing.com Motorsport Simulations, LLC**.

All trademarks, product names, company names, and logos (including “iRacing”) are the property of their respective owners.  
The use of any trade name or trademark is solely for identification and reference purposes and does **not imply any association** with the trademark holder or their product.

---

### 🏁 Useful Links

- [iR2mqtt App GitHub Repository](https://github.com/jmlt/ir2mqtt)  
- [HACS Documentation](https://hacs.xyz/docs/use)  
- [Home Assistant MQTT Integration](https://www.home-assistant.io/integrations/mqtt/)  
