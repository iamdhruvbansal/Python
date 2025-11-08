marks = input("Enter your marks: ")

try:
    marks = float(marks)   # Accepts both integers and decimals
    if marks < 0 or marks > 100:
        print("INVALID INPUT: Marks should be between 0 and 100")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("FAIL")
except ValueError:
    print("INVALID INPUT: Please enter a numeric value")