import sqlite3
import cv2
import random
#add photo
#all the databases stored.


def Creator(tb_name):
    conn = sqlite3.connect("Daaa.db")
    cursor = conn.cursor()
    create_table = "CREATE TABLE %s (id INT, photo TEXT,dob TEXT,age INT,bpl INT,mgneraga int,name TEXT)" %tb_name
    try:
        cursor.execute(create_table)
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        return "Table already Created, Or DATABASE is locked "

def Destructor(tb_name):
    conn = sqlite3.connect("Daaa.db")
    cursor = conn.cursor()
    q = "DROP TABLE %s" %tb_name
    cursor.execute(q)
    conn.commit()
    conn.close()
    
def Inserter(database,table_name):
    obj_values = ins()
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    insert_q = "INSERT INTO %s VALUES (?,?,?,?,?,?,?)" %table_name 
    cursor.execute(insert_q,obj_values)
    conn.commit()
    conn.close
    
def Printer(database,table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    insert_q = "SELECT * FROM %s" %table_name 
    for row in cursor.execute(insert_q):
        print(row)
    conn.commit()
    conn.close

def Printer_specific(database,table_name,obj_values):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    lis=[]
    insert_q = "SELECT * FROM %s WHERE mgneraga=%s" %(table_name,obj_values[0])
    for row in cursor.execute(insert_q):
        lis.append(row)
    return lis
    conn.commit()
    conn.close

    
def ins():
    id=2#from save file
    photo = "NULL"
    name=str(input("Enter the Namme here: "))
    dob = str(input("Enter the Date Of Birth here(day\month\year : "))
    age = int(input("Enter the Age here: "))
    bpl = int(input("Enter if bpl: "))
    mgnera = int(input("Does he wanna opt of mgnera? "))
    return [id,photo,dob,age,bpl,mgnera,name]

    
    
