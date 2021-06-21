import configparser

import mysql.connector
from mysql.connector import Error


def getconfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\Priyanka Mohaldar\\PycharmProjects\\Backendtesting\\MYAPI\\Utilities\\properties.ini')
    return config

connect_config = {
    'user': getconfig()['SQL']['user'],
    'password': getconfig()['SQL']['password'],
    'database': getconfig()['SQL']['database'],
    'host': getconfig()['SQL']['host']

}


def getconnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("conncetion is succesful")
            return conn
    except Error as e:
        print(e)
