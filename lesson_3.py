names = ["John", "SMITH", "ANDREW", "Julie", "Jackob"]
# print(names)


ages = [18, 28, 38, 50, 65]
# print(ages)

mixedLists = [15, 28, "Andrew", True]
# print(mixedLists)

# Last Index of names[-1]
# print(names[-1])

names[1] = "Arman"
# print(names)

# add from last
names.append("Ben")
# print(names)

# remove from last
names.pop()
#print(names)

# Takes last element
lastElement = names.pop()
# print(lastElement)

mixedLists2 = [
    ["James", "Kim", "Simon"],
    [15, 18, 39, 55, 78, 95, -16, 78]
]
# print(mixedLists2[1][2])
# print(mixedLists2[1][-1])

totalLists = mixedLists2[0] + mixedLists2[1]
# print(totalLists)

dubledLists = mixedLists2[0] * 2
# print(dubledLists)

# from first till 2nd element
# print(mixedLists2[1][2:])
# from first till (from last) 2nd element
print(mixedLists2[:-2])