names = ["Julie", "Simon", "John", "Andrew", "Kim"]

'''
for name in names:
    if name == "John":
        # continue # skip and continue from next of "John"
        break # return false, code will be stopped
    print(name)
'''

# range(0, 11) returns numbers from 0-10
'''
for number in range(0, 11):
    if number % 2 == 0 and number % 4 == 0:
        print(number)
'''


people = {
    "Julie":23,
    "Simon":28,
    "John":30,
    "Smith":55
}
for key, value in people.items():
    print(key)
    print(value)
    print("==========")
    