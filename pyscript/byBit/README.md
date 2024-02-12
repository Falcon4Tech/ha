# Home Assistant ByBit Portfolio Value Sensor

This integration adds a custom sensor to Home Assistant that retrieves and displays the portfolio value (in BTC) from the ByBit exchange. The script is designed to run periodically, fetching the latest data and updating the sensor accordingly.

## Installation

1. Copy the `assets.py` script to your Home Assistant configuration directory (e.g., `/config/pyscript/assets.py`).

2. Add the provided `sensor.yaml` configuration to your Home Assistant configuration file.

```yaml
command_line:
  - sensor:
      name: Bybit Portfolio Value
      unique_id: fc2fc32d-689b-42ca-9c64-3da4ba29747d
      command: 'python3 /config/pyscript/assets.py'
      value_template: "{{ value_json.sum }}"
      json_attributes:
        - price
      unit_of_measurement: BTC
      device_class: monetary
      state_class: measurement
      scan_interval: 1800
```

3. Restart your Home Assistant instance to apply the changes.

## Configuration

- `name`: The name of the sensor.
- `unique_id`: A unique identifier for the sensor.
- `command`: The command to run the Python script.
- `value_template`: The template to extract the sensor value from the script's output.
- `json_attributes`: Additional JSON attributes to extract and display.
- `unit_of_measurement`: The unit of measurement for the sensor.
- `device_class`: The device class for the sensor.
- `state_class`: The state class for the sensor.
- `scan_interval`: The interval (in seconds) between sensor updates.

## Notes

- Make sure you have the necessary API key and secret configured in the `config.py` file.

- The script uses the ByBit API to fetch the portfolio data and calculate the total value in BTC.

- Adjust the scan interval according to your preferences and the ByBit API rate limits.

Feel free to contribute, report issues, or suggest improvements!
