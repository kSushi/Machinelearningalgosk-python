# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:42:55 2020

@author: sushil.kasar
"""


import schedule
import time

def job():
    print("Reading time..")
    
def coding():
   print("Coding time..")

#Time
schedule.every(10).seconds.do(job)
schedule.every(5).seconds.do(coding)

while True:
   schedule.run_pending()
   time.sleep(1)    