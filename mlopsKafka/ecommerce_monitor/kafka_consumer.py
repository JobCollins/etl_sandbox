from kafka import KafkaConsumer
import json
import psycopg2
import configparser


# set up the consumer 
consumer = KafkaConsumer(
    'ecommerce_activity',
    bootstrap_servers = 'localhost:9092',
    auto_offset_reset = 'earliest', # start consuming from the beginning of the topic
    value_deserializer = lambda x:json.loads(x.decode('utf-8'))
)

# create a ConfigParser object
config = configparser.ConfigParser()
# read the configuration file
config.read('/Users/jobdulo/Documents/etl_sandbox/mlopsKafka/ecommerce_monitor/postgres_db_credentials.txt')

# establish connection to PostgreSQl
conn = psycopg2.connect(
    dbname=config.get('Credentials', 'db_name'),
    user=config.get('Credentials', 'username'),
    password=config.get('Credentials', 'password'),
    host=config.get('Credentials', 'host'),
    port=config.get('Credentials', 'port')
)

cursor = conn.cursor()

try:
    for message in consumer:
        data = message.value

        query = """
        INSERT INTO activity_log (user_id, activity_type, product_id, timestamp)
        VALUES (%s,%s,%s,%s);
        """
        cursor.execute(query, (data['user_id'], data['activity_type'], data['product_id'], data['timestamp']))

        conn.commit() # commit changes

        print(f"Stored: {data}")
except KeyboardInterrupt:
    pass
finally:
    cursor.close()
    conn.close()