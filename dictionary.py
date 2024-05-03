info = {
   "name":"Rijan",
   "faculty": "BCA",
   "college": "chitwan college of technology"
}

print(info)
print(type(info))

# accessing element from the dictionary

print(info["college"])

# get() -> it is used to get the value in the dictionary

faculty = info.get("faculty")
print(faculty)

# to update the value of given dictionary

info["name"] = "ujjwal"
print(info)

# to add the data in the dictionary we use
# update({"key": value})

info.update({"course":"python"})
print(info)

# to remove the dictionary item we use 
# pop("key")

product = {
    "name": "airpods",
    "price": 149.22,
    "category": "Gadgets",
    "quantity": 2,
    "review": 4.9,
}
print(product)

value_qunatity = product.pop('quantity')
print(product)
print(value_qunatity)

product.popitem()
print(product)

# looping through the dictionary

for i in product.items():
    print(i)

# to extract the keys of the dictionary
for keys in product.keys():
    print(keys)


# to extract the values of the dictionary
for values in product.values():
    print(values)

# to extract both keys and values

for key,value in product.items():
    print(f"{key} => {value}")
