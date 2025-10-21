# iR2mqtt – Home Assistant Integration

![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange)
![HACS Integration](https://img.shields.io/badge/HACS-Integration-blue)
![Release](https://img.shields.io/github/v/release/jmlt/ir2mqtt_integration)

Home Assistant integration for [iR2mqtt](https://github.com/jmlt/ir2mqtt). Automatically creates iRacing telemetry sensors from MQTT data.

---

<img width="1046" height="328" alt="ir3" src="https://github.com/user-attachments/assets/93c0253d-9d25-457c-8fc1-65d6018544fb" />
<img width="1579" height="614" alt="ir4" src="https://github.com/user-attachments/assets/ba99282c-c87e-4f3b-8eff-5aaec16558ed" />

---

## 🧩 Instalation step by step

https://github.com/jmlt/ir2mqtt/wiki/Home-Assistant

---

## ✨ Features

* **Automatic Discovery:** Automatically creates and configures sensors and binary sensors related to iRacing telemetry.  
* **Unified Device:** All entities are grouped under a single “iRacing Telemetry” device for a clean, organized structure inside Home Assistant.  
* **Included Sensors:**
  * **Sensors:** Speed (m/s, km/h, mph), RPM, Gear, Fuel Level, Current Lap, Session Time, Session Type, Incidents, Start Lights, and more.
  * **Binary Sensors:** On Pit Road, Active Flags (Green, Yellow, White, Blue, etc.), Start Lights (Ready, Set, Go).

---

## ⚠️ Disclaimer

This project is an **unofficial community integration** and is **not affiliated, associated, authorized, endorsed by, or in any way officially connected with**  
**iRacing.com Motorsport Simulations, LLC**.

All trademarks, product names, company names, and logos (including “iRacing”) are the property of their respective owners.  
The use of any trade name or trademark is solely for identification and reference purposes and does **not imply any association** with the trademark holder or their product.

---

### 🏁 Useful Links
- [Automation Example YAML](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/automation-example.yaml)
- [Home Assistant Community Post](https://community.home-assistant.io/t/ir2mqtt-bring-iracing-live-telemetry-to-home-assistant/901589)
- [iR2mqtt App GitHub Repository](https://github.com/jmlt/ir2mqtt)
- [HACS Documentation](https://hacs.xyz/docs/use)  
- [Home Assistant MQTT Integration](https://www.home-assistant.io/integrations/mqtt/)  
