def total(m1, m2, m3):
    return m1 + m2+ m3

def percentage(total_marks):
    return total_marks/3
def grade(percent):
    if percent >=90:
        return"A"
    elif percent >=75:
        return"B"
    elif percent >=60:
        return"C"
    else:
        return "D"
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
marks = total(m1, m2,m3)
percent = percentage(marks)

print("Total:",marks)
print("Percentage:", percentage(marks))
print("Grade:",grade(percent))