import logging

import psycopg2

from tests.helpers.test_data_utils import TestDataUtils


def connect_db():
    """Connect to Hermes"""
    try:
        connection = psycopg2.connect(
            user=get_db_credentials("user"),
            password="",
            host=get_db_credentials("host"),
            port=get_db_credentials("port"),
            database=get_db_credentials("database"),
        )
        logging.info("Connected to Hermes")

    except Exception as error:
        raise Exception(f"Error while connecting to Hermes '{str(error)}'")
    return connection


def get_db_credentials(variable):
    return TestDataUtils.TEST_DATA.db_details.get(variable)


def execute_query_fetch_one(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def execute_query_fetch_all(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def execute_update(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def clear_db(connection):
    if connection:
        connection.close()
