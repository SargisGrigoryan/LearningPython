data = {"John" : 2500, "Julie" : 1500, "Simon" : 3500}
# print(data)
#print(data["Julie"])

data2 = {
    "boys":["Arman","Rick","Andrew","Smith"],
    "girls":["Julie","Laura","Nicole","Kim"]
}

# print(data2["girls"])

# it will show none value instead of error if not found that key
# print(data.get("Arman"))

data["Julie"] = 2200
# print(data)

data2["girls"].append("Anna")
# print(data2)

# it just updates datas
data.update({"Julie":3600, "Simon":3300})
# print(data)

# it will returns only keys
# print(data2.keys())

# it will returns only values
print(data2.values())