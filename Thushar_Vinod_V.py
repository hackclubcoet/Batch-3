print(" WELCOME TO SUPERMARKET") #a welcome statement
sum = 0 #define sum as 0
dict = {'Sugar':40, 'Rice':30, 'Sanitizer':50, 'Soap':25, 'Brush':10, 'Pen':5, 'Book':20,

#Thushar Vinod V-3-Bill

        'Bag':150, 'Charger':100, 'Chocolate':60} #making a dictionary to store products and its prices

lst = list(dict.keys()) #making a list of keys in the dictionary and assigning this to a variable lst

while True: #while loop
    print(" No Product    Price")
    print(" 1. Sugar      40") # showing products and its prices
    print(" 2. Rice       30")
    print(" 3. Sanitizer  50")
    print(" 4. Soap       25")
    print(" 5. Brush      10")
    print(" 6. Pen         5")
    print(" 7. Book       20")
    print(" 8. Bag       150")
    print(" 9. Charger   100")
    print("10. Chocolate  60")
    print("Press B to calculate your bill") #for calculating bill

    product = input("Enter your product ") #using input funtion storing the value in a variable

    if product in lst: #if your entered product is in lst adding the prices
        sum += dict[product] #adding the prices and assigning value to sum
    elif product == 'B': #to calculate bill we use to enter B
        break #to break the statement
    else:
        print("Enter right product") #if your product is incorrect

print("Your total bill is : ", sum) #finally bill is calculated using sum variable
print(" THANK YOU")