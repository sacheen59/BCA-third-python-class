day = input("Enter your day: ")

match day:
    case "sunday":
        print("Day is sunday")
    case "monday":
        print("Day is monday")
    case _:
        print("Invalid day")
