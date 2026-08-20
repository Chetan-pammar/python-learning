username = input("Enter your username:")
valid = username.strip().isalnum()
if valid:
    print("Its Valid.")
else:
    print("Its Invalid")