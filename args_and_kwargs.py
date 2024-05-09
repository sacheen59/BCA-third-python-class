# def sum(a,b,*args):
#     temp = 0
#     for i in args:
#         temp = temp + i
    
#     print(temp)


# sum(10,20,30,40,50,60)

username =input("Enter username: ")
password = input("Enter password: ")

def loginCredentials(**kwargs):
    if kwargs["username"] == username and kwargs["password"] == password:
        print("login successful")
    else:
        print("login failed")


loginCredentials(username = "ujjwal", password = "*****", address = "bharatpur")




