import json
import pandas as pd
import requests
from sqlalchemy import create_engine
import configparser


# function to extract data from an API Aand convert data into a dataframe
def get_data():
    url = r"https://official-joke-api.appspot.com/random_ten"
    response = requests.get(url)
    data = json.loads(response.text)

    # normalize the semi-structure data and turn it into a df
    dataframe = pd.json_normalize(data=data)
    return dataframe

# function to save the data into a PostgreSQL db
def commit_to_postgres():

    # create a ConfigParser object
    # config = configparser.ConfigParser()
    # # read the configuration file
    # config.read('postgres_db_credentials.txt')

    # # read the credentials from file
    # username = config.get('Credentials', 'username')
    # host = config.get('Credentials', 'host')
    # password = config.get('Credentials', 'password')
    # port = config.get('Credentials', 'port')
    # db_name = config.get('Credentials', 'db_name')

    engine = create_engine(
        "postgresql://postgres:ColynX360@localhost:5432/jobdulo"
    )

    # sql syntax to create the table that would hold our data
    create_table_query = """ 
    CREATE TABLE jokes_data(
                type text,
                setup text,
                punchline text,
                id integer primary key
                ) 
            """

    # a raw database connection that allows direct interaction with the database
    connection = engine.raw_connection()

    # the cursor allows us to execute queries and retrieve results from the database
    cursor = connection.cursor()

    # creating the table using the cursor
    cursor.execute(create_table_query)

    # storing the result of the function into a variable
    dataframe = get_data()

    # pushing the data into the database
    for _, row in dataframe.iterrows():
        cursor.execute(
            "INSERT INTO jokes_data (id, type, setup, punchline) VALUES (%s, %s, %s, %s)",
            (
            row["id"],
            row["type"],
            row["setup"],
            row["punchline"]),
        )

    # committing the current transaction to the database
    connection.commit()

    # closing the cursor
    cursor.close()
    # closing the connection
    connection.close()


# calling our functions
get_data()
commit_to_postgres()

