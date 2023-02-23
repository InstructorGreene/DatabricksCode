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

# COMMAND ----------

varName = "variable"
var2Name = 12

var2Name -= 2

print(var2Name)

# COMMAND ----------

num1 = 14
num2 = 13

if num1 > num2:
    print("First number is greater")
elif num1 == num2:
    print("The numbers are equal")
else:
    print("The second number is greater")



# COMMAND ----------

#TASK

# ask for two numbers to be input, then display the larger of the two
# 

# COMMAND ----------

#Task

# write some code that will output to the screen if the year you were born was a leap year
# Hint: use the % operator


# 4, 8, 16
inputYear = input("What year were you born?")

if(int(inputYear) % 4 == 0):
    print("Born on a lap year partner")
else :
    print("Not born on a leap year")

# COMMAND ----------

#           0,1,2,3,4,5,6,7,8,9,10
products = [1,2,3,4,122,6,-65,"foo bar",8,18,18]




for counter in range(len(products)):
    print(counter, products[counter])


# COMMAND ----------

password = "openSesame1!"

entry = False

while entry != password:
    entry = input("Please enter your password")
    
print("Welcome in")

# COMMAND ----------

guess = False
while guess != "Rumplestiltskin":
    guess = input("guess my name")
print("correct")

# COMMAND ----------

while True:
    guess = input("guess my name")
    if guess == "Rumplestiltskin":
        print("Correct")
        break
    print("Wrong")
    
        

# COMMAND ----------

while True:
    guess = input("guess my name")
    if guess != "Rumplestiltskin":
        print("Wrong")
        continue
    print("Continue")
    break
        

# COMMAND ----------

#Task 
# Ask the user to enter a series of numbers

# Create a total by adding each number to the last

# Stop adding numbers when the user types zero 

# Print out the total at the end

total = 0 

while True:
    guess = input("next number?...")
    if(int(guess) == 0):
        break
    else:
        total += int(guess)
        print("Current total: ", total)
        
print(total)

# COMMAND ----------

import random


num = 3.1473


print(random.randint(1, 100))

# COMMAND ----------

#                parameter/argument
def printMessage(message):
    print(message)
    
    
printMessage("hello world")
printMessage("goodbye world")

# COMMAND ----------




def square(number):
    squaredNumber = number ** 2 
    return squaredNumber

    def outputter(num):
        print(num)

numToSquare = 5

answer = square(numToSquare)



print("the sqaure of " + str(numToSquare) + " is: ", answer)

# COMMAND ----------

# 1. Declare and test a function convert_to_kg to convert imperial pounds to kilograms 
# 1 kg = 2.2lb

# 2. Declare and test a function convert_to_celsius to convert a temperature given in Fahrenheit to Celsius. The formula is:
# degrees_celsius = (degrees_fahrenheit - 32)*(5/9)

# Test the functions:
# COnvert 100lbs to kg
# COnvert 20lbs to kilos

# Convert 32f to C
# Convert 100F to c


# COMMAND ----------

number_to_conv = 10

def temp_converter(num, bool):
    if(bool == False):
        return ((num - 32) * 5/9)
    else:
        return((num * 1.8) + 32)

    
    
temp_converter(10, True)


# COMMAND ----------

list1 = [[1,2,3], [4,5,6], [7,8,9]]

# 1,2,3
# 4,5,6
# 7,8,9

print(list1[2][1])



# COMMAND ----------

import random

my_list = ["i", "d","l", "e"]


# del my_list[2:4]
# my_list[1] = "n"
# new_list = ["s"] + my_list
# new_list.append("g")

# new_list.insert(1, "t")

final_list = []
for i in my_list:
    print(i, my_list.index(i))
    final_list.append(my_list.index(i))

print(final_list)

print(sum(final_list))
print(len(final_list))


# COMMAND ----------

# Create a list that contains ten integers your user has typed in at the keyboard.
user_input = []

for i in range(5):
    input_number = int(input("Input number " + str(i) + " , " + str(10-i) + " left"))
    user_input.append(input_number)
    

# Calculate & display the sum and average of the numbers stored in this new list.  
input_sum = sum(user_input)
input_average = input_sum / len(user_input)

print("input list is: ", user_input)
print("sum of the list is: " + str(input_sum))
print("average of the list is: " + str(input_average))


# Display each number in turn, along with a message stating whether it is below, above or equal to the average
for number in user_input:
    print(number)
    if number == input_average:
        print("Number is equal to average")
    elif number < input_average:
        print("Number is less then average")
    else:
        print("Number is greater then average")

# e.g. 10 is above average
