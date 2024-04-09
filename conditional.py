# conditional statement => if, elif, else

# day = "wednesday"

# if day == "tuesday":
#     print("we are learning python")
# else:
#     print("today is not tuesday")


# day = input("Enter the day: ")

# if day == "sunday":
#     print('Holiday in foreign country')
# elif day == "saturday":
#     print("holiday in Nepal")

# else:
#     print("It's not holiday")


number = int(input("Enter your number: "))

if number > 0:
    if number < 10:
        print("The number is between 0 and 10")
        
    print("positive number")
elif number < 0:
    print("negative number")
else:
    print("Zero")
