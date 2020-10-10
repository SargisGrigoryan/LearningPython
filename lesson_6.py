print("======== Menu ========")
print("1. Home")
print("2. Settings")
print("3. Profile")
print("4. Exit")

print("Enter Menu ID: ")
command = input()
login = True

if command == "1":
    print("Open Home Page")
elif command == "2":
    print("Open Settings")
elif command == "3" and login == True:
    print("Open Profile")
else:
    print("Exit Application")