def check_odd(num):
    return num % 2 == 0

numbers = [1,3,4,5,6,7,8,9]
odd_numbers = list(filter(check_odd, numbers))
print(odd_numbers)



def check_name(name):
    if len(name) % 2 == 0:
        return name[0]
    else:
        return name

names = ["ujjwal","Ram","kripesh","rijan","sijan"]
new_names = list(map(check_name, names))
print(new_names)