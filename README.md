## Overview

This project presents a comprehensive Internet of Things (IoT) solution for real-time monitoring and data analytics of an off-grid solar power system. Utilizing a Raspberry Pi 3 A+ as the edge computing device, the system seamlessly interfaces with an Outback FlexMax 80 charge controller through a custom-built adapter designed for MateNET—a proprietary communication protocol developed by Outback.

### Custom Adapter for MateNET
To establish a robust link between the Raspberry Pi and the charge controller, a specialized adapter was engineered to convert MateNET's UART signals to TTL levels suitable for the Pi. This adapter employs opto-isolators to ensure electrical isolation, safeguarding the Raspberry Pi from any voltage irregularities in the charging system. The adapter interfaces with the MateNET's standard RJ45 connector, adhering to its unique pin-out configuration, thus ensuring a secure and reliable connection.

### Data Collection and Storage
Data acquisition is managed by Telegraf, a versatile agent for collecting and reporting metrics. Once gathered, the metrics are forwarded to a cloud-hosted InfluxDB database. This cloud-based solution not only provides scalability but also ensures data security and integrity.

### Visualization and Analytics
For user-friendly, real-time analytics and visualization, the data stored in InfluxDB is rendered through Grafana Cloud. This provides an interactive platform to monitor various parameters such as battery voltage, current, and overall system health.

This end-to-end system offers a robust, secure, and highly interactive solution for monitoring various aspects of an off-grid solar energy setup, from data acquisition to visualization.


## Technologies Used

- Raspberry Pi
- MateMXDevice
- DHT11 Temperature and Humidity Sensor
- Python
- InfluxDB Cloud
- Grafana
- Telegram Bot API

## Features

- Real-time querying of multiple metrics
  - Battery Voltage and Current
  - PV (Photovoltaic) Voltage and Current
  - kWh (Kilowatt-hours)
  - Ah (Ampere-hours)
  - Temperature and Humidity
- Secure and scalable data storage using InfluxDB Cloud
- Real-time data visualization and analytics via Grafana
- Real-time alerting and data querying via Telegram Bot
