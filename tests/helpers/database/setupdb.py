import logging

import psycopg2

from settings import HERMES_DATABASE_URI, HARMONIA_DATABASE_URI
from tests.helpers.test_data_utils import TestDataUtils


def connect_db():
    """Connect to Hermes"""
    try:
        connection = psycopg2.connect(HERMES_DATABASE_URI)
        logging.info("Connected to Hermes")

    except Exception as error:
        raise Exception(f"Error while connecting to Hermes '{str(error)}'")
    return connection


def connect_harmonia_db():
    """Connect to Harmonia"""
    try:
        connection = psycopg2.connect(HARMONIA_DATABASE_URI)
        logging.info("Connected to Harmonia")

    except Exception as error:
        raise Exception(f"Error while connecting to Harmonia '{str(error)}'")
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
