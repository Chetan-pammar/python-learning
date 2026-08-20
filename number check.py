def check_number(number):
    if number > 0:
        return "Positive"
    elif number <0:
        return "Negative"
    else:
        return "Zero"

number = int(input("Enter a number: "))
answer = check_number(number)
print(answer)