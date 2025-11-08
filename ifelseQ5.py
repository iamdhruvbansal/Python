# Input a string from user and check whether it is numeric, alphabetic (uppercase/lowercase), alphanumeric or invalid input.

a = input("Enter something: ")

if a.isnumeric():
    print(f"{a} is a number")
elif a.isalpha():
    if a.isupper():
        print(f"{a} is uppercase alphabetic")
    elif a.islower():
        print(f"{a} is lowercase alphabetic")
    else:
        print(f"{a} contains both uppercase and lowercase letters")
elif a.isalnum():
    print(f"{a} is alphanumeric (letters and numbers)")
else:
    print(f"{a} is Invalid Input")