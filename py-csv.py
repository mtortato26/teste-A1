import csv
from multiprocessing.sharedctypes import Value
import mysql.connector

# Import

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="dbcsv"

)

# Conexão com a DB

with open('itens_mod.csv') as file:
    file = csv.reader(file, delimiter=',')
    all_value = []
    for tit in file:
        Value = (tit[0], tit[1], tit[2], tit[3], tit[4], tit[5], tit[6])
        all_value.append(Value)

query = "insert into `allcsv` (`group_id`,`material_id`,`item_qty`,`item_dim_1`,`item_dim_2`,`item_dim_3`,`item_class`) values (%s, %s, %s, %s, %s, %s, %s)"

# Abertura do .csv e inserção dos valores na DB 

mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()

