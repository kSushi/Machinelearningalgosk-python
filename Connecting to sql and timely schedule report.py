# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:50:25 2020

@author: sushil.kasar
"""


import pandas as pd
import numpy as np
import pymssql
import os
import datetime
from mattermostdriver import Driver
import schedule
import time

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def job():
    server1 = " "
    user1 = " "
    password1 = ""
    db_name1 = " "
    
    server = " "
    user = " "
    password = ""
    db_name = " "
    
    conn = pymssql.connect(server1, user1, password1, db_name1)
    
    sql_dz = """ SQL query
    """
    
    df_dz = pd.read_sql(sql_dz, conn) 
    
    conn = pymssql.connect(server, user, password, db_name)
    
    sql_usr ="""
              SQL query
    """
    df_usr = pd.read_sql(sql_usr, conn) 
    
    
    sql_jv = """SQL query
    
    """
    
    df_jv = pd.read_sql(sql_jv, conn) 
    df_dz = df_dz.merge(df_usr, on='', how='left')
    df_dz = df_dz.merge(df_jv, on='', how='left')
    
    df_dz = df_dz.loc[df_dz.##column]
    
    #import datetime
    df_dz[''] =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    
    from sqlalchemy import create_engine
    conn1 = create_engine('mssql+pyodbc://' + user1 + ':' + password1 + '@' + server1 + '/' +
                         #  db_name1 + '?driver=SQL+Server')
                         db_name1 + '?driver=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.3.so.1.1')
    test = conn1.connect()
    df_dz.to_sql(con=test, name=' ', if_exists='replace', index=False)
    test.close()
    conn1.dispose()
    
    print("Update at" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    
    
schedule.every(5).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(5)
    print('')
