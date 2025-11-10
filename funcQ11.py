def digitCheck(num):
    if (num<=9):
        print("Single Digit Number")
    elif (num<=99):
        print("Double Digit Number")
    elif (num<=999):
        print("Triple Digit Number")
    elif (num>999):
        print("Number contains more than three digits")
    else:
        print("Invalid Input: Try Again")

digitCheck(int(input("Enter the desired number: ")))
