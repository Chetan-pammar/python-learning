name = input("Enter your name:")
age = input("Enter your age:").strip()
completion_12=input("Have you completed 12th?(yes/no):")
print("Name=",name.strip().title())
if age.isdigit() and completion_12.strip().lower()=="yes":
    main_age=int(age)
    if main_age >=18:
        print(f"Age=\t{main_age}\nStatus=\tEligible")
    else:
        print(f"Age=\t{main_age}\nStatus=\tNot Eligible")
else:
    print("Age=\tInvalid Age\nStatus=\tNot Eligible")
