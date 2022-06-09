from ast import Delete
from tkinter.tix import TEXT
import psycopg2
conn=psycopg2.connect(database='postgres',user='postgres',password='spiderman001',host='127.0.0.1',port=5432)
cur=conn.cursor()

def new_contact():
      print('--CREATE NEW CONTACT--')
      cnt_name=input("Enter contact name:")
      cnt_number=int(input("Enter contact number:"))
      cnt_email=input("Enter contact email:")
      cnt_add=input("Enter contact address:")
      cur.execute('''INSERT INTO PHBK VALUES(%s,%s,%s,%s)''',[cnt_name,cnt_number,cnt_email,cnt_add])
      conn.commit()
      print("--CONTACT CREATED--")
      decision()
def view_all():
      print("--CONTACT BOOK--")
      cur.execute("SELECT * FROM PHBK ORDER BY CONTACT_NAME")
      res=cur.fetchall()
      for i in res:
            print("CONTACT NAME  : {0}\nCONTACT NUMBER  : {1}\nCONTACT EMAIL  : {2}\nCONTACT ADDRESS : {3}".format(i[0],i[1],i[2],i[3]))
      decision()
def search():
      search_param=int(input("---SEARCH BY-- \n[1]Name \n[2]Number \nYour option: "))
      if search_param==1:
            search_name=input("Enter name: ")
            cur.execute('''SELECT * FROM PHBK WHERE CNT_NAME=%s''',[search_name])
            search_result=cur.fetch()
            for i in search_result:
                  print("Contact Details:\nContact Name: {}\nContact Number: {}\nContact Email: {}\n Contact Address:".format(i[0],i[1],i[2],i[3]))
            decision()
      elif search_param==2:
            search_number=int(input("enter number: "))
            cur.execute('''SELECT * FROM PHBK WHERE CONTACT_NUMBER = %s''',[search_number])
            search_result=cur.fetchall()
            for i in search_result:
                  print("Contact Details:\nContact Name: {}\nContact Number: {}\nContact Email: {}\nContact Address:".format(i[0],i[1],i[2],i[3]))
            decision()
def delete():
      delete_param=int(input("[1] Delete a record\n [2] Delete all records"))
      if delete_param==1:
            delete_name=input("Enter Name :")
            cur.execute('''DELETE FROM PHBK WHERE CONTACT_NAME=%s''',[delete_name])
            print("--CONTACT DELETED--")
      if delete_param==2:
            cur.execute('''TRUNCATE TABLE PHBK''')
            print("--PHONE BOOK DELETED--")
      conn.commit()
      decision()

def decision():
      user_input=int(input("----Phone book----\n[1] Add new contact\n[2] View all contact\n[3] Search a contact\n[4] Delete \n[5] Exit \nYour option : "))
      if user_input==1:
            new_contact()
      elif user_input==2:
            view_all()
      elif user_input==3:
            search()
      elif user_input==4:
            delete()
      elif user_input==5:
            print("--Thank You---")
            
def banner():
      print('''                                                                                      
88888888ba   88        88  88888888ba     ,ad8888ba,      ,ad8888ba,    88      a8P   
88      "8b  88        88  88      "8b   d8"'    `"8b    d8"'    `"8b   88    ,88'    
88      ,8P  88        88  88      ,8P  d8'        `8b  d8'        `8b  88  ,88"      
88aaaaaa8P'  88aaaaaaaa88  88aaaaaa8P'  88          88  88          88  88,d88'       
88""""""'    88""""""""88  88""""""8b,  88          88  88          88  8888"88,      
88           88        88  88      `8b  Y8,        ,8P  Y8,        ,8P  88P   Y8b     
88           88        88  88      a8P   Y8a.    .a8P    Y8a.    .a8P   88     "88,   
88           88        88  88888888P"     `"Y8888Y"'      `"Y8888Y"'    88       Y8b  
                                                                                      
                                                                                      ''')
      decision()
banner()



'''cur.execute(CREATE TABLE PHBK (
      CONTACT_NAME VARCHAR,
      CONTACT_NUMBER BIGINT,
      CONTACT_EMAIL VARCHAR,
      CONTACT_ADDRESS TEXT
)'''