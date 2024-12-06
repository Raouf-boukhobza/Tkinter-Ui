import pymysql
import tkinter as tk
from tkinter import messagebox


def create_connection():
    try:
      connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="LocationDb"
        )
      print("Successfully connected using PyMySQL")
      return connection
    except Error as e:
        print(f"Error: '{e}' occurred")
        return None
    
    