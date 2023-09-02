import os
import requests
import csv
from io import StringIO
from telegram import Update
from telegram.ext import CommandHandler, Updater, CallbackContext

# Fetch tokens from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
INFLUX_TOKEN = os.getenv('INFLUX_TOKEN')

def create_query_handler(field_name, unit):
    def query_handler(update: Update, context: CallbackContext):
        # Replace with your InfluxDB URL
        url = "YOUR_INFLUXDB_URL_HERE"
        
        headers = {
            'Authorization': f'Token {INFLUX_TOKEN}',
            'Content-Type': 'application/vnd.flux',
            'Accept': 'text/csv'
        }
        
        # Replace 'YOUR_BUCKET_NAME' and 'YOUR_MEASUREMENT_NAME' with your bucket and measurement names
        data = f"""
        from(bucket: "YOUR_BUCKET_NAME") 
        |> range(start: -1h) 
        |> filter(fn: (r) => r._measurement == "YOUR_MEASUREMENT_NAME" and r._field == "{field_name}") 
        |> last()
        """
        
        response = requests.post(url, headers=headers, data=data)
        
        # Parse the response as CSV
        csv_reader = csv.DictReader(StringIO(response.text))
        value = 'N/A'  # Default value if the query returns no result
        for row in csv_reader:
            value = row['_value']
            break
        
        update.message.reply_text(f"The {field_name} is {value}{unit}")
        
    return query_handler

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    
    # Replace field names and units with those specific to your setup
    dp.add_handler(CommandHandler("vbat", create_query_handler("FIELD_NAME", "UNIT")))
    dp.add_handler(CommandHandler("abat", create_query_handler("FIELD_NAME", "UNIT")))
    dp.add_handler(CommandHandler("vpanel", create_query_handler("FIELD_NAME", "UNIT")))
    dp.add_handler(CommandHandler("apanel", create_query_handler("FIELD_NAME", "UNIT")))
    dp.add_handler(CommandHandler("temperature", create_query_handler("FIELD_NAME", "UNIT")))
    dp.add_handler(CommandHandler("humidity", create_query_handler("FIELD_NAME", "UNIT")))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

