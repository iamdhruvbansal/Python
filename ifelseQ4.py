num1=int(input("Enter first number: "))
if num1<10:
    print(f"{num1} is single digit number")
elif num1<100 and num1>9:
    print(f"{num1} is double digit number")
elif num1<1000 and num1>99:
    print(f"{num1} is three digit number")
else:
    print(f"{num1} has more than three digits")