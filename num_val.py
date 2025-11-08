num=input("Enter something: ")
if num.isdigit():
    print(f"{num} is number")
    print(f"The type of num is {type(num)}")
    num=int(num)
    print(f"The type of num after conversion is {type(num)}")   
else:
    print(f"{num} is not a number")