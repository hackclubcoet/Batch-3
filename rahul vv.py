user_input='random'
data=list()

def mylist():
    print("MY TO-DO LIST:")
    print("1.ADD AN ITEM:")
    print("2.VIEW ITEMS:")
    print("3.EXIT")

while user_input !='3':
    mylist()
    user_input=input("What you want to do?:")

    if user_input== 1:
        item=input("Enter your new todo:")
        data.append(item)
        print("your current todo is:"+str(item))
    elif user_input== 2:
        print("list of todo list")
        for items in data:
            print(items)
    elif user_input== 3:
        print("GOOD BYE")
    else:
        print("please enter a valid value")


