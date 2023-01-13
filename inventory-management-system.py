from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(host="localhost", 
                           user="root", 
                           passwd=" ")
cur=mydb.cursor()

cur.execute("Create database Shop_Management")
cur.execute("show databases")
for i in cur:
    print(i)

cur.execute('create table SHOP( ItemNo integer(3), ItemName varchar(30), Quantity integer(5), Price integer(5))')

cur.execute("show tables")
for i in cur:
    print(i)
