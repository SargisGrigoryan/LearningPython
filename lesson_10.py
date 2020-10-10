name = "Arman"

try:
    print(name)
except NameError as a:
    print(a)
except ValueError as b:
    print(b)
except Exception as c: # universal
    print(c)
else:
    print("Else Block")
finally:
    print("Some Errors Found")

print("Continue...")