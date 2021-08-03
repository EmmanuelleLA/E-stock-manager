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
    #Lecture du fichier qui contient le noms des produits
    f = open('product_data.csv')
    fichierCSV = csv.reader(f)
    listeX = []
    for ligne in fichierCSV:
    	x = ligne[0]
    	listeX.append(x)
    NameProduct=listeX[0]

    #Lecture du fichier qui contient url des images
    f = open('product_url.csv')
    fichier2CSV = csv.reader(f)
    listeX = []
    for ligne in fichier2CSV:
    	x = ligne[0]
    	listeX.append(x)

    UrlProduct=listeX[1]

    file = open('data_barcode.txt', "r")
    for line in file:
        quantuple=line.strip()
    file.close()

    #Insertion des données dans la BD

    sql = "INSERT INTO Products (id, Name, quantity, url) VALUES ( %s, %s, %s, %s)"
    #sql = "INSERT INTO `Products` (`id`, `Name`, `quantity`) VALUES (NULL, %s, %s)"
    val = (quantuple, NameProduct, "1" ,UrlProduct)
    cursor.execute(sql, val)
    cnx.commit()
except mysql.connector.Error as err:
        # print("err")
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
        #Ajoute 1 a la quantité
        res= res+1
        #Update de la quantité
        sql_update_query = """UPDATE Products SET quantity = %s WHERE id = %s"""
        input_data = (res, quantuple)
        cursor.execute(sql_update_query, input_data)
        cnx.commit()


else:
    cnx.close()
