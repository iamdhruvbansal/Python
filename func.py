def greeting():
    print("Hello Everyone!")

def welcome(name):
    if name == "":
        print("Welcome, Guest!")
    else:
        print(f"Welcome, {name}!")

def add(num1,num2):
    return num1 + num2

greeting()
welcome("")
welcome("Alice")

#result = add(5, 10)
#print(f"The sum is: {result}")
print("Result of addition:", add(20, 30))