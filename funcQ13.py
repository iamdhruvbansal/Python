def grade(marks):
    try:
        marks=float(marks)
        if marks < 0 or marks > 100:
            print("Enter the value in between 0 to 100")
        elif marks >= 90:
            print("GRADE:A")
        elif marks >= 75:
            print("GRADE:B")
        elif marks >= 50:
            print("GRADE:C")
        else:
            print("FAIL")
    except ValueError:
        print("Invalid Input")

grade(input("Enter your marks: "))