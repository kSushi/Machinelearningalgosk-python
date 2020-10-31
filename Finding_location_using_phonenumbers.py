# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:46:49 2020

@author: sushil.kasar
"""


import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
phone_number1=phonenumbers.parse("+91XXXXXXX")
print(phone_number1)
print(geocoder.description_for_number(phone_number1,'en'))
print(carrier.name_for_number(phone_number1,'en'))
