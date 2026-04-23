---
title: "Graphing Zigbee2MQTT sensors with widgets"
category: Tutorial
summary: "Turn Zigbee2MQTT sensor values into MQTT graph widgets you can monitor from your iPhone Home Screen."
date: 2026-04
---
## What you'll need
- A running Zigbee2MQTT instance connected to Home Assistant or standalone
- A Zigbee sensor publishing a numeric value like temperature, humidity, or power

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
3. Paste in your topic and set the property path to the value you want to plot
4. Tap **Add to Home Screen**

Your sensor data will now appear as a graph on your Home Screen. If you want
to combine multiple Zigbee2MQTT sensors into one dashboard-style widget, use
an EasyMQTT Plus multi-graph widget instead.
