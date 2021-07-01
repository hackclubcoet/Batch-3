#Mohammed_Fayiz-batch3-password_generator
#if the user provide length and numbers of the password,password can be generated
import random
char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
'''CHARACTER OF PASSWORD IS TAKEN FROM THIS LIST '''
while 1:
    '''these function takes input from char list'''
    password_len  =int(input("please enter the length of the password required:-  "))
    password_count=int(input("how many passwords would you like to have?  "))
    for x in range(0,password_count):
        password  =''
        for x in range(0,password_len):
            password_char=random.choice(char)
            '''this function gives the required random password'''
            password     =password+password_char
        print("your required password is: ",password)