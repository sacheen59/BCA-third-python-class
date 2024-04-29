fruit_set = {"apple","banana","papaya","apple"}
print(fruit_set)

# length
print(len(fruit_set))

# add item to the set

fruit_set.add("orange")
print(fruit_set)

# to update the element of one set into another

city = {"pokhara","bharatpur","birgunj","biratnagar"}
famous_place = {"pokhara","biratnagar","jomsom","chitwan sauraha"}

city.update(famous_place)
print(city)

# to remove the set element use remove() or discard()

meatItem = {"mutton","chicken","pork","buff"}

# meatItem.remove("orange")
meatItem.discard("orange")
print(meatItem)

number = {1,2,3,4,5}
second_number = {2,3,4,5}

print(number.union(second_number))
print(number.intersection(second_number))
print(number.difference(second_number))
print(number.isdisjoint(second_number))