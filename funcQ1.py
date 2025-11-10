def table(num):
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1


table(int(input("Enter any number: ")))