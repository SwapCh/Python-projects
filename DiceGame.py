from random import sample

def dice():
    numbers = ["1", "2", "3", "4", "5", "6"]
    while True:
        user = input("Press 1 to play 0 to quit: ")
        user = int(user)
        if user not in [0, 1]:
            print("Please enter a valid input")
        elif user == 0:
            print("Thank You!")
            break
        else:
            print(sample(numbers, 1))


dice()
