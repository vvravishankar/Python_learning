import random

print("Let Play the Number Guessing Game")
print("Please select the number range for guessing")

# take user input for range
min = int(input("Lets select the min range:- "))
max = int(input("Lets select the max rang:- "))

# take a random integer with in the range
ran_number = random.randint(min,max)
#print(ran_number)

counter = 0
# taking while loop for input
while True:
    user_input = int(input("Guess the number:- "))
    counter = counter+1
    if user_input > max or user_input < min:
        print("your guess is out of range")
        counter = counter-1
    else:
        if user_input > ran_number:
            print("your guess is too high")
        elif user_input < ran_number:
            print("your guess is too low")
        else:
            print(f"You Guess the number in {counter} attempt")
            break






