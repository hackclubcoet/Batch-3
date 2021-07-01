user_name = input("!!! ENTER USERNAME !!!\n")  # prompts user to enter the user name
password = int(input("!!! ENTER PASSWORD !!!\n"))  # prompts user to enter the password

# Muhammed_Nadeer_CP-BATCH3-simple_login_page
# checks whether the entered username and password is correct or not
if(user_name == 'admin') and (password == 345):
    print("*** ACCESS GRANTED ***")
else:
    print("*** ACCESS DENIED ***")
