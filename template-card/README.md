# Home Assistant Template Card for Sensors

This Home Assistant template card displays sensor data, allowing you to monitor various attributes such as temperature, humidity, battery level, and signal strength. The card is designed to handle undefined values gracefully, ignoring them to avoid rendering errors.

## Features

- **Dynamic Sensor Attribute Monitoring**: You can set the attribute to be monitored (e.g., temperature, humidity, battery, signal strength).
- **Multiple Sensor Support**: Easily extend the card to include multiple sensors.
- **Graceful Handling of Undefined Values**: The card will ignore undefined values, preventing any rendering issues.
- **Time Since Last Update**: Display the time since each sensor's last update in hours or minutes.
- **Visual Indicator**: Provides a visual representation of the sensor attribute value.

## Usage

To use this card in your Home Assistant configuration use `markdown` card and follow these steps:

1. **Set the Attribute to Monitor**: Define the attribute you want to monitor (e.g., "battery"). 
2. **List Your Sensors**: Add the list of sensor IDs you want to include in the card.

```yaml
{% set attr = "battery" %}
{% set sensors = [
  "sensor_1",
  "sensor_2",
  "sensor_3",
  "sensor_4"
] %}
```

3. Ensure all sensor IDs end with the attribute specified in `attr`.

```yaml
sensor.sensor_1_battery
sensor.sensor_2_battery
sensor.sensor_3_battery
sensor.sensor_4_battery
```

## Example

Here's an example of how the card would look in your Home Assistant UI:

```
🟩 ◼︎◼︎◼︎◼︎   100% |  45m | Sensor 1
🟨 ◼︎◼︎◼︎    060% |  30m | Sensor 2
🟥 ◼︎      020% |   5m | Sensor 3
🆘        000% |   2m | Sensor 4
```

In this example, the card shows four sensors with their respective attribute values, visual indicators, and time since the last update.

## Notes


This template card is a flexible and robust solution for monitoring various sensor attributes in your Home Assistant setup. Customize the `attr` and `sensors` variables to suit your needs, and enjoy a seamless, error-free display of your sensor data.