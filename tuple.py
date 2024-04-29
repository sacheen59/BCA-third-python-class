fruits = ('apple','mango','papaya','banana','dragonfruit')

# to find the length
print(len(fruits))

print(type(fruits))

# tuple slicing
print(fruits[0])
print(fruits[-1])

list_fruits = list(fruits)
list_fruits.append("orange")
fruits = tuple(list_fruits)
print(fruits)

# joining two tuple

pNumber = (1,2,3,4,5)
nNumber = (-1,-2,-3,-4)

number = pNumber + nNumber
print(number)

duplicatePNumber = pNumber * 3
print(duplicatePNumber)