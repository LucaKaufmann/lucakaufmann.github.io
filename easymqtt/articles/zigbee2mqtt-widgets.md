---
title: "Graphing Zigbee2MQTT sensors with widgets"
category: Tutorial
summary: "Turn your z2m temperature and humidity readings into live sparklines on the Home Screen in five minutes."
date: 2026-04
---
## What you'll need
- EasyMQTT Plus (required for graph widgets)
- A running Zigbee2MQTT instance connected to Home Assistant or standalone
- A Zigbee sensor publishing temperature or humidity

## Step 1 - Connect to your broker
Open EasyMQTT and connect to the broker your Zigbee2MQTT instance
publishes to. If you're running Home Assistant, this is usually
`homeassistant.local` on port `1883`.

## Step 2 - Find your topic
In the Subscribe tab, subscribe to `zigbee2mqtt/#`. Watch the message
stream and find the topic for your sensor - it'll look like
`zigbee2mqtt/my-sensor/temperature`.

## Step 3 - Create a graph widget
1. Go to the Widgets tab and tap **+**
2. Choose **Graph widget**
3. Paste in your topic and set the property path to `temperature`
4. Tap **Add to Home Screen**

Your sensor data will now appear as a live sparkline on your Home Screen,
refreshing in the background every few minutes.
