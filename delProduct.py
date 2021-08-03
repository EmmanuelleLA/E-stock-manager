import mysql.connector
from mysql.connector import Error
import sys
import os
import csv
from subprocess import check_output
from subprocess import Popen, PIPE
import unicodedata
from random import *
import subprocess
import functools

try:
    cnx = mysql.connector.connect(  host="localhost", user="root", password="root", database="Projet_tut")
    cursor = cnx.cursor()

        #Recupere la quantiter du produit
    sql_Query = "SELECT quantity FROM Products WHERE id = %s"
    file = open('data_barcode.txt', "r")
    for line in file:
        quantuple=line.strip()
    file.close()
    id=(quantuple,)
    cursor.execute(sql_Query, id)
        # cursor.execute("SELECT quantity FROM Products WHERE id = 1")
    valQuantity = cursor.fetchone()
        #Transforme me tuple en int
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, valQuantity)


    if res ==0:
        # print("delete")
        sql_update_query = """DELETE FROM Products WHERE id = %s"""
        input_data = (id)
        cursor.execute(sql_update_query, input_data)
        cnx.commit()
    else :

        res= res-1
    #     #Update de la quantité
        sql_update_query = """UPDATE Products SET quantity = %s WHERE id = %s"""
        input_data = (res, quantuple)
        cursor.execute(sql_update_query, input_data)
        cnx.commit()

except mysql.connector.Error as err:
        print("err")
