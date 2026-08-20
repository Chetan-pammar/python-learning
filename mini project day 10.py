name = input("Enter your full name:")
age= input("Enter your age:")
country= input("Enter your country:")
username = input("Enter your username:")
fullname=name.strip().title()
print("Name:\t",fullname.title())
if age.isdigit():
    print("Age:\t",age)
else:
    print("Age:\tinvalid age")
if country.strip().lower()=="india":
    print("You are from India.\nValid")
else:
    print("You are not from India.\nInvalid")

if username.strip().isalnum():
    print("Username:\t",username.capitalize())
    print("Status:\tValid Username")
else:
    print("Username:\tInvalid")
    print("Status:\tInvalid Username")

