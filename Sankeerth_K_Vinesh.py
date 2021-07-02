# A bank software which allows user to login to their account and check their account details
username = input('Enter Your Username')
pin = input('Enter Your 4 Digit Pin')
# Sankeerth K Vinesh - Batch 3 - ATM
print('You Have Successfully Logged In')
# This program asks the input their username and password and let to log in

print('\n1 Account Details\n2 Account Balance\n3 Transaction History')
choice = int(input('Enter Your Choice'))
# This displays the activities and ask the user for their choice

if choice == 1:
    print('\nAccount Name:' + username+'\nAccount Number:789456123\nBank Branch:Gold Street Branch')
# This prints the account details of the user if users enters 1
elif choice == 2:
    print('\nAccount Balance:4500 rs')
# This prints the balance in the account if user enters 2
elif choice == 3:
    print('\nTransactions\n12/12/21\twithdrawal\t8000\n20/10/21\tdeposit\t\t12500')
# This prints the transaction details of the user if they enters 3
else:
    print('You Have Entered A Wrong Value')
# This says the user that the entered value is wrong if user enters other values
