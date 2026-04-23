---
title: "Home Assistant + EasyMQTT: a quick start"
category: Guide
summary: "Connect EasyMQTT to your Home Assistant broker, monitor MQTT topics live, and trigger scenes from Shortcuts."
date: 2026-03
---
## Prerequisites
- Home Assistant with the MQTT integration enabled
- EasyMQTT installed on your iPhone or iPad

## Connect to your broker
In Home Assistant go to **Settings -> Integrations -> MQTT** and note
your broker host (usually `homeassistant.local`) and port (`1883`).
Open EasyMQTT, tap **+** on the Connect screen, and enter those details.
If your broker uses authentication or TLS, enter those details here too,
then save the broker so you can reuse it in widgets and Shortcuts later.

## Subscribe to Home Assistant topics
Enable the MQTT statestream integration in your `configuration.yaml`:

```yaml
mqtt_statestream:
  base_topic: homeassistant
  publish_attributes: true
```

In EasyMQTT, subscribe to `homeassistant/#` to see all entity state
changes stream in live. If you only care about a few devices, you can
subscribe to narrower topics instead of watching the full tree.

## Trigger a scene with Siri
1. Open the Shortcuts app and tap **+**
2. Search for **EasyMQTT** -> pick **Send Message**
3. Set topic: `homeassistant/scene/evening/set`, payload: `ON`
4. Add to Siri with a phrase like "Hey Siri, evening mode"

Your Home Assistant scene now fires from your voice. From there, you can
save the same message as a favorite in EasyMQTT or build a bigger Shortcut
flow around it.
