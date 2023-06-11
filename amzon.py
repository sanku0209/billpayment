import math
import random

email1 = "saitejasanku26@gmail.com"
pass1 = 1212
email2 = input("Enter Your Email: ")
pass2 = int(input("Enter Your Password: "))

# List to store prices of items
item_prices = []
# List to store items we select
item_select = []

def cart():
    print("Your item added to the cart")
    check()

def bill():
    total_bill = sum(item_prices)
    print("...............................................")
    print("Your Total Bill is", total_bill)
    print("...............................................")
def select():
    print("Your selected items are")
    for i,j in zip(item_select,item_prices):
        print(i,"==",j)
    print()        
  

def eleprice():
    sub = [10000, 20000, 30000, 40000]
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    p = int(input("Enter Your Price: "))
    item_prices.append(sub[p - 1])
    cart()

def dressprice():
    sub = [1250, 2700, 3500, 4000]
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    p = int(input("Enter Your Price: "))
    item_prices.append(sub[p - 1])
    cart()

def cosprice():
    sub = [500, 1000, 1500, 2000]
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    p = int(input("Enter Your Price: "))
    item_prices.append(sub[p - 1])
    cart()

def groprice():
    sub = [1000, 1500, 2000, 2500]
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    p = int(input("Enter Your Price: "))
    item_prices.append(sub[p - 1])
    cart()

def ele(n):
    sub = ['Mobile', 'TV', 'AC', 'Fridge']
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    #item_select.append(sub[num - 1])
    def mobile(num):
        sub = ['Apple', 'Realme', 'One+', 'Redmi']
        for i in range(len(sub)):
            print(i + 1, ":", sub[i])
        sel = int(input("Select Your Brand: "))
        if n == 1 or 2 or 3 or 4:
            print(".........................................")
            print("You selected", sub[sel - 1])
            print(".........................................")
            eleprice()

    def tv(num):
        sub = ['Sony', 'Samsung', 'Onida', 'LG']
        for i in range(len(sub)):
            print(i + 1, ":", sub[i])
        sel = int(input("Select Your Brand: "))
        if n == 1 or 2 or 3 or 4:
            print("..............................")
            print("You selected", sub[sel - 1])
            print("..............................")
            eleprice()

    def ac(num):
        sub = ['Samsung', 'LG', 'BlueStar', 'Godrej']
        for i in range(len(sub)):
            print(i + 1, ":", sub[i])
        sel = int(input("Select Your Brand: "))
        if n == 1 or 2 or 3 or 4:
            print("........................................")
            print("You selected", sub[sel - 1])
            print("........................................")
            eleprice()

    def fridge(num):
        sub = ['LG', 'Godrej', 'Whirlpool', 'Haier']
        for i in range(len(sub)):
            print(i + 1, ":", sub[i])
        sel = int(input("Select Your Brand: "))
        if n == 1 or 2 or 3 or 4:
            print("..............................")
            print("You selected", sub[sel - 1])
            print("..............................")
            eleprice()

    num = int(input("Select thing You want to buy: "))
    if num == 1:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        mobile(num)
        
    elif num == 2:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        tv(num)

    elif num == 3:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        ac(num)
     
    elif num == 4:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        fridge(num)
        

def dress(n):
    sub = ['Shorts', 'T-shirts', 'Shirts', 'Pants']
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    def com(num):
        sub = ['NetPlay', 'Denim', 'Levis', 'Uspolo']
        for i in range(len(sub)):
            print(i + 1, ":", sub[i])
        sel = int(input("Select Your Brand: "))
        if n == 1 or 2 or 3 or 4:
            print("..............................")
            print("You selected", sub[sel - 1])
            print("..............................")
            dressprice()

    num = int(input("Select thing You want to buy: "))
    if num == 1:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        com(num)
    elif num == 2:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        com(num)
    elif num == 3:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        com(num)
    elif num == 4:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        com(num)

def cos(n):
    sub = ['Lipsticks', 'Facewash', 'Creams', 'Makeup kit']
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    def com(num):
        sub = ['Himalaya', 'Eva', 'Ponds', 'Lakme']
        for i in range(len(sub)):
            print(i + 1, ":", sub[i])
        sel = int(input("Select Your Brand: "))
        if n == 1 or 2 or 3 or 4:
            print("..............................")
            print("You selected", sub[sel - 1])
            print("..............................")
            item_select.append(sub[num - 1])
            cosprice()

    num = int(input("Select thing You want to buy: "))
    if num == 1:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        com(num)
    elif num == 2:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        com(num)
    elif num == 3:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        com(num)
    elif num == 4:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        com(num)

def gro(n):
    sub = ['Rice bag', 'Pulses', 'Flours', 'Snacks']
    for i in range(len(sub)):
        print(i + 1, ":", sub[i])
    num = int(input("Select thing you want to buy: "))
    if num == 1 or 2 or 3 or 4:
        print("..............................")
        print("You selected", sub[num - 1])
        print("..............................")
        item_select.append(sub[num - 1])
        groprice()

def check():
    print(".................................................")
    remv = input("Do you Want to Continue (y/n):- ").lower()
    print(".................................................")
    if remv == "y":
        again()
    elif remv == "n":
        select()
        bill()
        number = int(input("Enter mobile number: "))
        d = '01234556789'
        otp = ' '
        for i in range(4):
            otp += d[random.randint(0, 9)]
        print('Your OTP is', otp)
        ot = int(input("Enter Your OTP: "))
        if int(otp) == ot:
            print("Transaction Successful")
            #select()
            #bill()
        else:
            print("OTP entered is wrong....")

if (email1 == email2) and (pass1 == pass2):
    def again():
        while True:
            print("...Category...")
            cat = ['Electronics', 'Dresses', 'Cosmetics', 'Grocery']
            for i in range(len(cat)):
                print(i + 1, ":", cat[i])
            n = int(input("Select Your Category: "))
            if n == 1:
                print("..............................")
                print("You selected", cat[n - 1])
                print("..............................")
                ele(n)
                break
            elif n == 2:
                print("..............................")
                print("You selected", cat[n - 1])
                print("..............................")
                dress(n)
                break
            elif n == 3:
                print("..............................")
                print("You selected", cat[n - 1])
                print("..............................")
                cos(n)
                break
            elif n == 4:
                print("..............................")
                print("You selected", cat[n - 1])
                print("..............................")
                gro(n)
                break
    again()
else:
    print("Invalid Credentials")
