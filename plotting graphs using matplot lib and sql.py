# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:01:02 2020

@author: sushil.kasar
"""


import pandas as pd
import numpy as np
import pymssql
import os
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


server = " "
user = " "
password = " "
db_name = " "

conn = pymssql.connect(server, user, password, db_name)

base_query = """
                        """
                        
base = pd.read_sql(base_query,conn)        
### run a for loop here
base.head()
df=base
df.head(50)
df['cum_count']=  df.groupby(['day']).collection.cumsum() #new column
### output 1
import matplotlib.pyplot as plt


plt.style.use('seaborn-whitegrid')

#plt.plot([df.month==7].day.values, df[df.month==7].cum_count.values, '--r', label='July 20')
#plt.plot([df.month==8].day.values, df[df.month==8].cum_count.values, ':b', label='Aug 20')
#plt.plot([df.month==9].day.values, df[df.month==9].cum_count.values, 'k', label='Sep 20')



plt.plot(df[df.month==7].day.values, df[df.month==7].cum_count.values, '--r', label='July 20')
plt.plot(df[df.month==8].day.values, df[df.month==8].cum_count.values, ':b', label='Aug 20')
plt.plot(df[df.month==9].day.values, df[df.month==9].cum_count.values, 'k', label='Sep 20')


plt.legend()
plt.axes().set(title='Day wise count of cumulative');
plt.axis('tight')
plt.xlabel("Days of the month")
plt.ylabel("Number of cumulative in the month")
