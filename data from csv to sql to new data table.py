# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:50:06 2020

@author: sushil.kasar
"""


import pymssql
import pandas as pd
from time import sleep
from pytz import timezone
from datetime import datetime
from sqlalchemy import create_engine

def job(): #creating function
    tid = pd.read_csv('campaign_TIDs.csv') #Reading csv file
    tid = tuple(tid.TID.astype(str).values) #Using column name TID from the csv file read.
    
    conn = pymssql.connect(server, user, password, db_name)

    
    sql1 =       """
    
                 """
    d1 = pd.read_sql(sql1.format(tid), conn) #Reading SQL query with the csv column name {tid} format is used to store the tid's in sql query--autofill
    sql2 = """
    
          """
    d2 = pd.read_sql(sql2.format(tid), conn)
    
    day = '2020-11-01' # yyyy-mm-dd
    TPV = """
    
    """ #Sql query
    tpv1 = pd.read_sql(TPV.format(day, tuple(d1.tid), day, tuple(d1.tid)), conn) #tid is the field from csv and sql tables.
    try:
        tpv2 = pd.read_sql(TPV.format(day, tuple(d2.column_name), day, tuple(d2.column_name)), conn)
    except:
        pass
    conn.close()
    
    f1 = pd.merge(d1, tpv1, how='inner', right_on='tid', left_on='tid') #merge
    f1["new columns"] = f1.apply(lambda x: True if (x.last_tx_day - x.Created_On).days <=7 else False, axis="columns")
    f1 ["new columns"] = f1.apply(lambda x: (x.last_tx_day - x.Created_On).days, axis="columns")
    f1["new columns"] = f1.apply(lambda x: (datetime.now() - x.last_tx_day).days, axis="columns")
    #mention conditions
    z = pd.concat([f1.query(),
                   f1.query(),
                   f1.query(),
                   f1.query()], sort=False)
    z.Created_On = pd.to_datetime(z.Created_On)
    z.Ticket_Date = pd.to_datetime(z.Ticket_Date)
    z.Ticket_Closed_Date = pd.to_datetime(z.Ticket_Closed_Date)
    
    #database_name = create_engine(CREATE_ENGINE)
    con = #database_name.connect()
    z.to_sql(con=con, name='sql table name', if_exists='replace', index=False)
    con.close()
    #database_name.dispose()    

if __name__ == '__main__':
    while True:
        hr = int(datetime.now(timezone('Asia/Kolkata')).time().hour)
        minute = int(datetime.now(timezone('Asia/Kolkata')).time().minute)
        if minute%30 == 3:
            job()
            sleep(60)
        else:
            print(hr, minute)
            sleep(50)