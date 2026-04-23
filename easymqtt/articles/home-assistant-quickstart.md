---
title: "Home Assistant + EasyMQTT: a quick start"
category: Guide
summary: "Point EasyMQTT at your HA broker, subscribe to statestream, and fire off Siri commands that toggle scenes."
date: 2026-03
---
## Prerequisites
- Home Assistant with the MQTT integration enabled
- EasyMQTT installed on your iPhone or iPad

## Connect to your broker
In Home Assistant go to **Settings -> Integrations -> MQTT** and note
your broker host (usually `homeassistant.local`) and port (`1883`).
Open EasyMQTT, tap **+** on the Connect screen, and enter those details.
Leave username and password blank unless you've configured auth.

## Subscribe to statestream
Enable the MQTT statestream integration in your `configuration.yaml`:

```yaml
mqtt_statestream:
  base_topic: homeassistant
  publish_attributes: true
```

In EasyMQTT, subscribe to `homeassistant/#` to see all entity state
changes stream in live.

## Trigger a scene with Siri
1. Open the Shortcuts app and tap **+**
2. Search for **EasyMQTT** -> pick **Send Message**
3. Set topic: `homeassistant/scene/evening/set`, payload: `ON`
4. Add to Siri with a phrase like "Hey Siri, evening mode"

Your Home Assistant scene now fires from your voice.
