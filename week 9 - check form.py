import re


class Validation_Tools:
    valid_email = r"^(\S+)@(\S+)\.(\S+){2,3}$"
    valid_username = r"^(\w+){4,8}$"
    valid_password =  r"^(\w+){8,15}$"

    def check_email(self, input_email):
        if(re.match(self.valid_email, input_email)):
            print("Your email is valid")
            print()
            return True
        else:
            print("Email is not in valid form! Please try again!")
            print()
            return False


    def check_age(self, input_age):
        if(input_age in range(18, 65)):
            print("Your age is valid")
            print()
            return True
        else:
            print("Invalid Age! Please try again!")
            print()
            return False


    def check_username(self, input_username):
        if(re.match(self.valid_username, input_username)):
            print("Your username is valid")
            print()
            return True
        else:
            print("Your username is valid! Please try again!")
            print()
            return False


    def check_password(self, input_password):
        if(re.match(self.valid_password, input_password)):
            print("Your username is valid")
            print()
            return True
        else:
            print("Your username is valid! Please try again!")
            print()
            return False


class User:

    def __init__(self, username, password, email, age):
        self.username = username
        self.password = password
        self.email = email
        self.age = age


    def get_name(self):
        return self.username
    

    def welcome(self):
        print("Thank you for chosing us!")
        


def main():
    print("- Validation Input Form -")
    print()

    validate = Validation_Tools()

    while True:
        username = str(input("Input Username: "))
        if validate.check_username(username): break

    while True:
        password = str(input("Input Password: "))
        if validate.check_password(password): break

    while True:
        email = str(input("Input Email: "))
        if validate.check_email(email): break

    while True:
        age = int(input("Input age: "))
        if validate.check_age(age): break
    
    print("Your account is activated!")
    print()

    new_user = User(username, password, email, age)
    new_user.welcome()


if __name__ == "__main__":
    main()