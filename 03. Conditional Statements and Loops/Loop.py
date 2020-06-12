# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:29:44 2020

@author: pravin
"""

#Loops 
# 1.FOR Loop 
# 2. WHILE Loop

# 1. FOR Loop
#FOR Loop executes the condition till the last element is reached
        
Names = ["JOE","JOHN","MICHEAL","CLIFTON"]

for i in Names:
    print(i)
    
for i in range(10): #This will print all the values from 0 to 9. this will exclude the upper limit
    print(i)
    
number = [1,6,20,33]

for a in number:
    b = a*a    #This condition will give the square values of all the elements in  number
    print(b)
    
#Nested FOR loops
    
vegetables = ["potato","onion","cabbage"]
color = ["brown","yellow","green"]

#The below condition will give the combinations of veetables and color

for a in vegetables:
    for b in color:
        print(a,",",b)
    
# 2. WHILE Loops
        
a = 20

while a < 30: #This is the condition where a < 30
    print("Digit:", a) #This will print the value of a
    a = a+1  #This will add +1 until a is equal to 30
    

#Example
    
import random #imports the package random

rand1 = int(30*random.random()) #Creating a random number between 0 and 30

count = 0 #Defining the value of count as 0
while count != rand1: #Count is not equal to rand1
    count = int(input("Enter a number: ")) #Takes a new value from the user
    if count > 10: #Checks if count is > 10
        print("count is greater than 10")
    else: #Executes if count < 10
        print("count is smaller than 10")
else: #Executes if count is equal to rand1
    print("Count is equal to rand1")

