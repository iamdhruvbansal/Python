def vote(age):
    if age>=18:
        print("User is eligible for voting")
    else:
        print("User is not eligible for voting")

vote(int(input("Enter your age: ")))