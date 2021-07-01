import random
import math

# Nahida Sajid-3-Number Guessing
# Taking inputs
lower = int(input("Enter lower bound:-"))
upper = int(input("Enter upper bound:-"))

# Generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)), "chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# For calculation of minimum number of guesses depend upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number:-"))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in", count, "try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If Guessing is more than required Guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
