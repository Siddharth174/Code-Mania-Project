import random
num = random.randint(1, 100)
i = 0
print("GUESSING GAME")
print("You have 5 chances to guess")
while i != 5:
    guess = int(input("Enter your guess (any number between 1 to 100): "))
    if guess < num:
        print("Low")
    elif guess > num:
        print("High")
    else:
        print("Correct Answer!")
        break
    i += 1
if i == 5:
    print(f"Correct Answer is {num}")
