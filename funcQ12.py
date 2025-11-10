def input_val(a):
    if a.isnumeric():
        print("This is the numeric input")
    elif a.isalpha():
        if a.isupper():
            print("Input contains Uppercase letters")
        elif a.islower():
            print("Input contains Lowercase letters")
        else:
            print("Input contains both uppercase & lowercase letters")
    elif a.isalnum():
        print("Input contains both alphabets & numbers")
    else:
        print("INVALID INPUT")

input_val(input("Enter the desired input: "))