# Solar-System-Monitor-PyMate
IoT to monitor off-grid solar system. I used a raspberry pi 3 A+ to connect to an Outback FlexMax 80 charge controller. Telegraf was used to retrieve data to InfluxDB cloud which I connected to Grafana cloud to display the solar system data

# Solar Power Monitoring and Analytics System

## Overview

This project aims to develop a robust Solar Power Monitoring and Analytics System using Raspberry Pi, MateMXDevice, DHT11 sensor, InfluxDB Cloud, Grafana, and a Telegram Bot for real-time monitoring and alerts.

## Overview

This project embodies an end-to-end Internet of Things (IoT) solution for monitoring an off-grid solar power system. Leveraging a Raspberry Pi 3 A+ as the edge computing device, the system interfaces with an Outback FlexMax 80 charge controller to gather real-time metrics about the solar setup. Data retrieval is facilitated by Telegraf, an agent for collecting and reporting metrics, which then forwards the data to a cloud-based InfluxDB instance. This cloud storage solution not only offers scalability but also ensures data security. To provide a user-friendly interface for real-time analytics and visualization, the stored metrics are displayed through Grafana Cloud. This comprehensive setup offers a robust, secure, and interactive way to monitor various aspects of an off-grid solar system.


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
- Real-time alerting via Telegram Bot

## Installation and Setup

1. **Step 1**: [Description]
2. **Step 2**: [Description]
3. **Step 3**: [Description]

## Usage

```bash
[Command to run your program]
