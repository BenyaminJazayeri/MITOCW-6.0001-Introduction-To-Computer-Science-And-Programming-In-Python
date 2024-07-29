# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:21:06 2021

@author: Beny
"""


portion_down_payment = 0.25
current_savings = 0
r = 0.04 #annual return
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) #each month
total_cost = float(input("Enter the cost of your dream home: "))

ms = 0
while(current_savings<total_cost*portion_down_payment):
    current_savings += (annual_salary/12)*portion_saved + current_savings*r/12
    ms += 1
print("Number of months: ", ms)
    


