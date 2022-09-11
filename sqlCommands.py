import discord
import random
import asyncio
import sys
import time
import json
import requests
import datetime
import traceback
from discord.ext import commands
from discord.ext.commands import Bot

import tokendef
from tokendef import *
import definitions
from definitions import *
import helpStrings
from helpStrings import *

from PyDictionary import PyDictionary
from random_word import RandomWords

import mysql.connector
from mysql.connector import Error
import pandas as pd

#for custom commands via sql
#connect to server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#connect to specific db in server
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#regular query function, but print statements are specifically for db creation
def create_database(connection, query):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}''")

    return cursor

#execute regular query function
def execute_query(connection, query):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Query '{query}' successful")
    except Error as err:
        print(f"Error: '{err}'")

    return cursor
#create and keep open a mysql connection
connection = create_db_connection(host, username, password, db)  

