# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:50:23 2021

@author: Beny
"""
import numpy

portion_down_payment = 0.25
r = 0.04 #annual return
starting_annual_salary = float(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = .07
ms = 36

high = 10000
low = 1
portion_saved = (high + low)/2.0


current_savings = 0
num_steps=0
while abs(current_savings - total_cost*portion_down_payment) > 100 :
    

    if num_steps>numpy.log2(10000)+1:
        print("It is not possible to pay the down payment in three years.")
        break
        
    portion_saved /= 10000
    current_savings = 0
    annual_salary = starting_annual_salary
    for i in range(1,ms+1):
        if i%6==0:
            annual_salary *= (1+semi_annual_raise) 
        current_savings += (annual_salary/12)*portion_saved + current_savings*r/12
            
    portion_saved *= 10000 
    
    if current_savings > total_cost*portion_down_payment :
        
        high = portion_saved
        portion_saved = (high + low)/2.0
    
    else:
        
        low = portion_saved
        portion_saved = (high + low)/2.0
        
    num_steps+=1
    

        

if num_steps<numpy.log2(10000):    
    print("Best savings rate:",portion_saved/10000)
    print("Steps in bisection search:",num_steps)

