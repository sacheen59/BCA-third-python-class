
def check_square(num):
    return num ** 2


# list of numbers

numbers = [1,2,3,4,5,6,7,8,9,10]

square_numbers = list(map(check_square,numbers))
print(square_numbers)


multiplication = list(map(lambda num: num*2, numbers))
print(multiplication)