#!/usr/bin/python2.7
import os
import time
import json
import datetime
import requests
from dateutil.parser import parse

# Third-party libraries
import Adafruit_DHT
from pymate.matenet import MateNET, MateMXDevice
from settings import SERIAL_PORT

# Logging setup
import logging
logging.basicConfig(level=logging.INFO)

# Get environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4

# Function to check and send battery voltage alerts
def check_bat_voltage_and_send_telegram(voltage):
    bot_token = TELEGRAM_TOKEN
    chat_ids = os.getenv('CHAT_IDS').split(',')  # Assuming chat_ids are comma-separated in an env variable
    
    last_message_file = os.path.join(os.path.expanduser('~'), 'pymate', 'last_message_time.txt')

    current_time = datetime.datetime.now()

    # Read the last message time from a file
    if os.path.exists(last_message_file):
        with open(last_message_file, 'r') as file:
            last_message_time_str = file.read().strip()
            last_message_time = parse(last_message_time_str) if last_message_time_str else None
    else:
        last_message_time = None

    if voltage < 22 and (last_message_time is None or (current_time - last_message_time).total_seconds() > 8 * 60 * 60):
        message = f'Your battery voltage has dropped below: {voltage} volts!'
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        
        for chat_id in chat_ids:
            data = {'chat_id': chat_id, 'text': message}
            response = requests.post(url, data=data)

        # Update the last message time in a file
        with open(last_message_file, 'w') as file:
            file.write(current_time.isoformat())

# Main function
def main():
    bus = MateNET(SERIAL_PORT)
    port = bus.find_device(MateNET.DEVICE_MX)
    mate = MateMXDevice(bus, port)
    mate.scan()

    try:
        status = mate.get_status()
        # Rest of the code
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
