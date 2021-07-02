


#POULY BABU-3-CURRENCY CONVERTER

def convert_dollar(dollar): 
    '''a function to convert dollars to rupees'''
    rupee=dollar*74.28 
    return rupee

def convert_rupee(rupee):
    '''a function to convert rupees to dollars'''
    dollar=round(rupee/74.28,2 )
    return dollar 

'''asks the user to enter a choice'''
print("To convert dollar to rupee:press 1")
print("To convert rupee to dollar:press 2")

print("Your choice:",end='') 
choice=int(input())

'''checks which choice is entered'''
if choice==1:
    '''if choice is 1 asks the user to enter the amount'''
    print("Enter amount in USD:",end='')
    '''calls the function convert_dollar'''
    dollar=float(input())
    print("Amount in INR:",convert_dollar(dollar))

elif choice==2:
    '''if choice is 2 asks the user to enter the amount'''
    print("Enter amount in INR:",end='')
    rupee=float(input())
    '''calls the function convert_rupee'''
    print("Amount in USD:",convert_rupee(rupee))

else:print("!!WRONG CHOICE!!")
   




