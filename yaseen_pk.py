import time


# Yaseen PK-B3-HELLO WORLD(ANIMATION)

# This function takes in a string and returns it one character at a time

def delayed_string(string_name):
    for element in string_name:
        time.sleep(1)
        print(element, end='')


delayed_string("Hello world")