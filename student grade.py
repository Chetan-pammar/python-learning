def calculate_total(a, b, c):
    return a + b + c
def calculate_percentage(total):
    return total/3
def get_grade(percentage):
    if percentage>=90:
        return "A"
    elif percentage>=75:
        return "B"
    elif percentage>=60:
        return "C"
    else:
        return "D"

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

total = calculate_total(m1, m2, m3)
percentage = calculate_percentage(total)
grade = get_grade(percentage)

print("Total:",total)
print("Percentage:",percentage)
print("Grade:", grade)