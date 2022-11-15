import mysql.connector


try:
    conn = mysql.connector.connect(user='root',password='Sarth0310',database='mydata',host='localhost',port='3306')
    if(conn.is_connected):
        print("Connected")
except:
    print("Unable to connect")
'''
myc = conn.cursor()
myc.execute('CREATE DATABASE mydata')
myc.close()
conn.close()
'''

'''
sql = 'CREATE TABLE pharma(Reference_No INT AUTO_INCREMENT PRIMARY KEY,Company_Name VARCHAR(50),Types_of_Medicine VARCHAR(50),Medicine_Name VARCHAR(50),issu_Date VARCHAR(20),Exp_Date VARCHAR(20),Uses VARCHAR(50),Dosage INT,Product_QT INT,Tablets_Price FLOAT,Total_Price FLOAT)'
myc=conn.cursor()
myc.execute(sql)
myc.close()
conn.close()
'''

sql1 = 'INSERT INTO pharma(Company_Name,Types_of_Medicine,Medicine_Name,issu_Date,Exp_Date,Uses,Dosage,Product_QT,Tablets_Price,Total_Price) VALUES("Serum","Injection","Anti-Covid","11-12-2021","25-12-2023","For Covid-19 and only for 18+",1,5,300,1500),("Patanjali","Tablet","FIght-Covid","1-2-2020","5-1-2023","For Covid-19 and only for 18+",1,10,150,1500)'
sql1 = 'UPDATE pharma SET Types_of_Medicine="Tablet" WHERE Reference_No = 4'
myc = conn.cursor()
try:
    myc.execute(sql1)
    conn.commit()
    print(myc.rowcount,'row insert')
    #print(myc.lastrowid,'current id')
except:
    conn.rollback()
    print('unable to insert data')
myc.close()
conn.close()