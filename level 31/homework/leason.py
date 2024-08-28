def name_uppercase(name):
    print(name.upper())



def name_lowercase(name):
    print(name.lower())


def request_password(correct_password):
    while True:
        user_password = input("enter password: ")
        if user_password == correct_password:
            print("true!")
            break
        else:
            print("false")


