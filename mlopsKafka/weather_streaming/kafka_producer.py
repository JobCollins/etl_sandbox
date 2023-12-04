from kafka import KafkaProducer
import json # send JSON-formatted data
import time # time related tasks like sleep
import random # simulate weather data using random values

# create the producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# generate random weather data 
WEATHER_STATES = ['Sunny', 'Rainy', 'Windy', 'Cloudy', 'Snowy']

while True:
    weather = random.choice(WEATHER_STATES)
    temperature = random.randint(-5, 35) # temperatures from -5C to 35C
    humidity = random.randint(10, 90) # humidity percentage

    # send weather data to the topic
    message = f"Weather: {weather}, Temperature: {temperature}C, Humidity: {humidity}%"
    producer.send('weather_forecasts', value=message.encode('utf-8'))
    time.sleep(5) # send every 5 seconds

