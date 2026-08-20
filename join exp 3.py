cars = input("Enter any 3 cars:")
suv = cars.split()
print("-".join(suv))

ame = input("Enter your name:")
age = input("Enter your age:")
completion_12=input("Have you completed 12th?(yes/no)")
print("Name=",name.strip().title())
if age.isdigit() and completion_12.strip().lower()=="yes":
    if age>=18:
        print("Age=\t",age.strip())
    else:
        print("Age=\tunderage")
else:
    print("Invalid Age.")
if completion_12.strip().lower()=="yes":
    print("Eligible")
else:
    print("Not Eligible")
