# Welcome to treasure hunt game.Your objective is to find the treasure without getting killed
print("Would you like to go left or right?")
direction = input().lower()
# Vaishak_Bharathan-Batch3-Treasure Hunt
# asking user for inputting directions
if direction == "right":
    print("GAME OVER")
    # if user enters right game over
elif direction == "left":
    print("You can either choose to swim or wait")
    n = input().lower()
# asking user whether he wants to swim or wait
    if n == "wait":
        print("choose a door:Red,Blue or Yellow")
        door = input().lower()
        # asking user to choose any one of the coloured doors
        if door == "blue":
            print("EATEN BY BEASTS,GAME OVER")
        elif door == "red":
            print("BURNED BY FIRE,GAME OVER")
        elif door == "yellow":
            print("YOU WIN")
        else:
            print("GAME OVER")
    else:
        print("ATTACKED BY TROUT,GAME OVER")
