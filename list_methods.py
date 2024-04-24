fruits = ["apple","mango","banana","papaya","orange"]

# updating the list item
fruits[0] = "pineapple"
print(fruits)

# adding the item in the list 
fruits.append("dragonfruit")
print(fruits)

# inserting the element of the list in certain index
fruits.insert(2,"pumpkin")
print(fruits)

# to append the whole list element from the another list

number = [1,2,3,4,5]
print(number)
nextNumber = [6,7,8,9,10]
number.extend(nextNumber)
print(number)

# to remove the item from the list

area= ["bharatpur","tandi","geetanagar","baseni"]
# remove(value)
area.remove("baseni")
print(area)

#pop(index)=> removes the element of given index and also return value

firstIndexValue = area.pop(0)
print(area)
print(firstIndexValue)

# del => use to delete the given index element and also it is use to delete the entire list

facebookPost = ["dashin","tihar","sports","travel"]
del facebookPost[0]
print(facebookPost)

# del facebookPost
# print(facebookPost)

#clear() => it delete all the element from the list but the list still exists

facebookPost.clear()
print(facebookPost)


# sorting the list element

numbers = [2,38,7,9,0,1,8]
print("====before sorting====")
print(numbers)
print("====after sorting====")
numbers.sort(reverse=True)
print(numbers)



