import string
import random

def generate_password(theLenght):
    ''' This function generates password '''
    letters = string.ascii_letters
    digits = string.digits
    totalChars = letters + digits
    finalResult = ""
    for i in range(theLenght):
        finalResult += random.choice(totalChars)
    
    return finalResult

def main():
    while True:
        print("Enter the password lenght")
        theLenght = input()
        
        try:
            theLenght = int(theLenght)
        except:
            print("Wrong password lenght")
            continue
        
        thePassword = generate_password(theLenght)
        print("The Password is : " + thePassword)

main()