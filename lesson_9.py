def print_hellow(fromWho, to):
    print("Hello from " + fromWho + " to " + to)

# print_hellow("Julie", "Andrew")

def sum(numberOne=0, numberTwo=0):
    print(numberOne + numberTwo)

sum(5, 6)
sum(100, 200)

'''
myVar = "Some Text"
varTwo = 598
print(type(myVar))
print(type(varTwo))
print(type(str(varTwo)))
'''

'''
import os

dirpath = os.getcwd()

print("Current Directory: " + dirpath)

from datetime import datetime
print(datetime.today())
'''

def doubled(x):
    x *= 2
    return x

finalResult = doubled(10)
# print(finalResult)

myString = "Hello World"
def changeString():
    global name
    name = "Arman"

changeString()
print(name)
# print(myString)