# Databricks notebook source
#here be some STRINGS
first_name = "redacted" 
second_name = "fdsfsd"

#here be booleans
bool1 = True
bool2 = False

# here be integers
int1 = 10
int2 = 1000000
int3 = -23

# here be floats
float1 = 1.23
float2 = -3.333333

# here be a list 
list1 = [12,12,23,24,45]
list_product = ["saw", 'banjo', "screwdriver"]

print(list_product)

print(first_name + " " +second_name)

# COMMAND ----------


number1 = 17
number2 = 5

print("sum: ", number1 + number2) 
print("subtraction: ", number1 - number2) 
print("mult: ", number1 * number2) 
print("div: ", number1 + number2) 

print("Integer Division: ", number1 // number2) 
print("Modulo: ", number1 % number2) 

# COMMAND ----------

number1 = input("please enter a number")
number2 = input("enter a second")

print(int(number1) + int(number2))
