import mysql.connector
from mysql.connector import Error

# MySQL 연결 정보로 연결
def get_connection():
    return mysql.connector.connect(
    host='localhost',
    user='user', #'your_username',
    password='1234',#'your_password'
    database='codingon'
)