name = input("Enter your name:")
age = input("Enter your age:").strip()
country= input("Enter your country:")
username= input("Enter your username")
completion_12th=input("Have you completed 12th?(yes/no):")
print("Name:\t",name.strip().title())
if age.isdigit() and country.strip().lower()== "india" and completion_12th.strip().lower()== "yes" and username.strip().isalnum(): 
    main_age = int(age)
    if main_age>=18:
        print("Status:\tEligible.")
    else:
        print("Status:\tNot Eligible under age")
else:
    print("Status:\tNot Eligible")