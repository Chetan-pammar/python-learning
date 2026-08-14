
username = input("Enter your username:")
password = input("ENter your password:")
name = username.strip().lower()
print("========LOGIN========")
if username.strip().lower()=="chetan" and password == "Chetan@999":
    print(f"Login Successful!\nWelcome {name}")
else:
    print("Invalid username or password.")
print("====================")