from random import *
import datetime

def calculateEstimate(cart):
    estimate = 0
    percentage = 0
    for key in cart:
        if key != "UID":
            estimate += cart[key][0]*cart[key][1]
    percentage = (estimate/100)*20
    estimate = estimate + percentage
    return estimate

def createCart():
    cart = {}

    print("**-------Component Order------**")
    cart["UID"] = randint(1, 10000)
    print("What processor do you want?")
    print("Option 1: p3")
    print("Option 2: p5")
    print("Option 3: p7")
    print("")
    processor = 0
    while processor != 1 and processor != 2 and processor != 3:
        processor = int(input())
        if processor != 1 and processor != 2 and processor != 3:
            print("")
            print("Error: invalid input - input option number only")
            print("")
            print("What processor do you want?")
    print("")
    print("How many do you want?")
    proAmount = int(input())
    print("")
    if processor == 1:
        cart["p3"] = [100, proAmount]
    elif processor == 2:
        cart["p5"] = [120, proAmount]
    elif processor == 3:
        cart["p7"] = [200, proAmount]
    print("**-----------------------------**")

    print("How much RAM do you want?")
    print("Option 1: 16GB")
    print("Option 2: 32GB")
    print("")
    ram = 0
    while ram != 1 and ram != 2: 
        ram = int(input())
        if ram != 1 and ram != 2:
            print("")
            print("Error: invalid input - input option number only")
            print("")
            print("How much RAM do you want?")
    print("")
    print("How many do you want?")
    ramAmount = int(input())
    print("")
    if ram == 1:
        cart["16GB"] = [75, ramAmount]
    elif ram == 2:
        cart["32GB"] = [150, ramAmount]
    print("**-----------------------------**")

    print("How much storage do you want?")
    print("Option 1: 1TB")
    print("Option 2: 2TB")
    print("")
    storage = 0
    while storage != 1 and storage != 2:
        storage = int(input())
        if storage != 1 and storage != 2:
            print("")
            print("Error: invalid input - input option number only")
            print("")
            print("How much storage do you want?")
    print("")
    print("How many do you want?")
    storageAmount = int(input())
    print("")
    if storage == 1:
        cart["1TB"] = [50, storageAmount]
    elif storage == 2:
        cart["2TB"] = [100, storageAmount]
    print("**-----------------------------**")

    print("What screen size do you want?")
    print("Option 1: 19inch")
    print("Option 2: 23inch")
    print("")
    screen = 0
    while screen != 1 and screen != 2:
        screen = int(input())
        if screen != 1 and screen != 2:
            print("")
            print("Error: invalid input - input option number only")
            print("")
            print("What screen size do you want?")
    print("")
    print("How many do you want?")
    screenAmount = int(input())
    print("")
    if screen == 1:
        cart["19inch"] = [65, screenAmount]
    elif screen == 2:
        cart["23inch"] = [120, screenAmount]
    print("**-----------------------------**")

    print("What type of case do you want?")
    print("Option 1: Mini Tower")
    print("Option 2: Midi Tower")
    print("")
    case = 0
    while case != 1 and case != 2:
        case = int(input())
        if case != 1 and case != 2:
            print("")
            print("Error: invalid input - input option number only")
            print("")
            print("What type of case do you want?")
    print("")
    print("How many do you want?")
    caseAmount = int(input())
    print("")
    if case == 1:
        cart["Mini Tower"] = [40, caseAmount]
    elif case == 2:
        cart["Midi Tower"] = [70, caseAmount]
    print("**-----------------------------**")

    print("How many USB ports do you want?")
    print("Option 1: 2 Ports")
    print("Option 2: 4 Ports")
    print("")
    usb = 0
    while usb != 1 and usb != 2:
        usb = int(input())
        if usb != 1 and usb != 2:
            print("")
            print("Error: invalid input - input option number only")
            print("")
            print("How many USB ports do you want?")
    print("")
    print("How many do you want?")
    usbAmount = int(input())
    print("")
    if usb == 1:
        cart["2 Ports"] = [10, usbAmount]
    elif usb == 2:
        cart["4 Ports"] = [20, usbAmount]
    print("**-----------------------------**")

    return cart

def estimate(cart):
    estimate = calculateEstimate(cart)
    print("**---------Estimate--------**")
    for key in cart:
        if key == "UID":
            print(key, ": ", cart[key])
        else:
            print(key, ": ", (cart[key][0]*cart[key][1]))

    print("The estimated price of your order is: ", estimate)
    print("**----------------**")
    return estimate

def checkStock(cart, stock):
    flag = 0
    for key in stock: #Enter component type
        for letter, number in stock[key].items(): # Select component and amount
            for key1 in cart: # Enter shopping cart
                if letter == key1: # Compare component with cart item
                    if number < cart[key1][1]: # Compare the amounts for each item
                        print("Stock Error (", key, ": ", letter, "): Insufficient Stock Levels")
                        flag+=1
    if flag >= 1:
        return False
    elif flag == 0:
        return True

def correctStock(cart, stock):
    for key in stock:
        if key == "Processors":
            for key1 in cart:
                if key1 == "p3":
                    stock[key].update({"p3": stock[key]["p3"]-cart[key1][1]})
                elif key1 == "p5":
                    stock[key].update({"p5": stock[key]["p5"]-cart[key1][1]})
                elif key1 == "p7":
                    stock[key].update({"p7": stock[key]["p7"]-cart[key1][1]})
        if key == "RAM":
            for key1 in cart:
                if key1 == "16GB":
                    stock[key].update({"16GB": stock[key]["16GB"]-cart[key1][1]})
                elif key1 == "32GB":  
                    stock[key].update({"32GB": stock[key]["32GB"]-cart[key1][1]})
        if key == "Storage":
            for key1 in cart:
                if key1 == "1TB":
                    stock[key].update({"1TB": stock[key]["1TB"]-cart[key1][1]})
                elif key1 == "2TB": 
                    stock[key].update({"2TB": stock[key]["2TB"]-cart[key1][1]})
        if key == "Screen":
            for key1 in cart:
                if key1 == "19inch":
                    stock[key].update({"19inch": stock[key]["19inch"]-cart[key1][1]})
                elif key1 == "23inch": 
                    stock[key].update({"23inch": stock[key]["23inch"]-cart[key1][1]})
        if key == "Case":
            for key1 in cart:
                if key1 == "Mini Tower":
                    stock[key].update({"Mini Tower": stock[key]["Mini Tower"]-cart[key1][1]})
                elif key1 == "Midi Tower": 
                    stock[key].update({"Midi Tower": stock[key]["Midi Tower"]-cart[key1][1]})
        if key == "USB Ports":
            for key1 in cart:
                if key1 == "2 Ports":
                    stock[key].update({"2 Ports": stock[key]["2 Ports"]-cart[key1][1]})
                elif key1 == "4 Ports": 
                    stock[key].update({"4 Ports": stock[key]["4 Ports"]-cart[key1][1]})
        
    return stock

def checkCart(cart):
    print()
    inputUser = 0
    if cart != 0:
        inputUser = input("Do you wish to use your estimate order (y/n): ")
        if inputUser == "y" or inputUser == "Y":
            return cart
        elif inputUser == "n" or inputUser == "N":
            tempCart = createCart()
            return tempCart
        elif (inputUser != "y" or inputUser != "Y") and (inputUser != "n" or inputUser != "N"):
            print()
            print("Error: Invalid input. Please enter y or n.")

def placeOrder(cart, stock, estimate, date):
    print()
    customer = []
    customer = getCustomerDetails()
    cart["Customer"] = customer
    cart["Date"] = date[0]
    printShop(cart, estimate) #Simulate shop receipt
    printCustomer(cart, estimate) #simulate customer copy
    stock = correctStock(cart, stock)
    return stock

def dailyOrderList(orderNumber):
    #Over view of whole day
    print() #Display all details of every order made in session
    print("**--------Daily Overview--------**")
    print("Item Number\tOrder Id\tPrice")
    print("--------------------------------------")
    count = 1
    total = 0
    for i in orderNumber:
        print ("Item ", count, end="\t\t")
        for key, value in i.items():
            if key == "UID":
                print (value, end="  \t\t")
            elif key == "Estimate":
                print (value, end="")
                total+=value
        count+=1
        print("")
    print("--------------------------------------")
    print("Daily Net Total: \t\t", total)
    print("**----------------------------------**")
    print()

    print("**------------Components Sold----------**")
    items1 = {'Processors': {'p3': 0, 'p5': 0, 'p7': 0}, 'RAM': {'16GB': 0, '32GB': 0}, 'Storage': {'1TB': 0, '2TB': 0}, 'Screen': {'19inch': 0, '23inch': 0}, 'Case': {'Mini Tower': 0, 'Midi Tower': 0}, 'USB Ports': {'2 Ports': 0, '4 Ports': 0}}
     
    for key in items1:
        if key == "Processors":
            for i in orderNumber:
                for key1, value in i.items():
                    if key1 == "p3":
                        items1[key].update({"p3": items1[key]["p3"]+value[1]})
                    elif key1 == "p5":
                        items1[key].update({"p5": items1[key]["p5"]+value[1]})
                    elif key1 == "p7":
                        items1[key].update({"p7": items1[key]["p7"]+value[1]})
        if key == "RAM":
            for i in orderNumber:
                for key1, value in i.items():
                    if key1 == "16GB":
                        items1[key].update({"16GB": items1[key]["16GB"]+value[1]})
                    elif key1 == "32GB":  
                        items1[key].update({"32GB": items1[key]["32GB"]+value[1]})
        if key == "Storage":
            for i in orderNumber:
                for key1, value in i.items():
                    if key1 == "1TB":
                        items1[key].update({"1TB": items1[key]["1TB"]+value[1]})
                    elif key1 == "2TB": 
                        items1[key].update({"2TB": items1[key]["2TB"]+value[1]})
        if key == "Screen":
            for i in orderNumber:
                for key1, value in i.items():
                    if key1 == "19inch":
                        items1[key].update({"19inch": items1[key]["19inch"]+value[1]})
                    elif key1 == "23inch": 
                        items1[key].update({"23inch": items1[key]["23inch"]+value[1]})
        if key == "Case":
            for i in orderNumber:
                for key1, value in i.items():
                    if key1 == "Mini Tower":
                        items1[key].update({"Mini Tower": items1[key]["Mini Tower"]+value[1]})
                    elif key1 == "Midi Tower": 
                        items1[key].update({"Midi Tower": items1[key]["Midi Tower"]+value[1]})
        if key == "USB Ports":
            for i in orderNumber:
                for key1, value in i.items():
                    if key1 == "2 Ports":
                        items1[key].update({"2 Ports": items1[key]["2 Ports"]+value[1]})
                    elif key1 == "4 Ports": 
                        items1[key].update({"4 Ports": items1[key]["4 Ports"]+value[1]})                     
    for key in items1:
        if key == "Processors":
            if items1[key]["p3"] > 0:
                print("p3: ",items1[key]["p3"])
            if items1[key]["p5"] > 0:
                print("p5: ",items1[key]["p5"])
            if items1[key]["p7"] > 0:
                print("p7: ",items1[key]["p7"])
        if key == "RAM":
            if items1[key]["16GB"] > 0:
                print("16GB: ",items1[key]["16GB"])
            if items1[key]["32GB"] > 0:
                print("32GB: ",items1[key]["32GB"])
        if key == "Storage":
            if items1[key]["1TB"] > 0:
                print("1TB: ",items1[key]["1TB"])
            if items1[key]["2TB"] > 0:
                print("2TB: ",items1[key]["2TB"])
        if key == "Screen":
            if items1[key]["19inch"] > 0:
                print("19inch: ",items1[key]["19inch"])
            if items1[key]["23inch"] > 0:
                print("23inch: ",items1[key]["23inch"])
        if key == "Case":
            if items1[key]["Mini Tower"] > 0:
                print("Mini Tower: ",items1[key]["Mini Tower"])
            if items1[key]["Midi Tower"] > 0:
                print("Midi Tower: ",items1[key]["Midi Tower"])
        if key == "USB Ports":
            if items1[key]["2 Ports"] > 0:
                print("2 Ports: ",items1[key]["2 Ports"])
            if items1[key]["4 Ports"] > 0:
                print("4 Ports: ",items1[key]["4 Ports"]) 
    print("**----------------------------------**")

    i = 0
    print() #Display all details of every order made in session
    print("**------------Order Details----------**")
    print()
    for i in orderNumber:
        count = 0
        for key, value in i.items():
            if count == 0:
                print("\t**--------Order ", value ,"--------**")
                count +=1
            if key == "UID":
                print("\t", key, ": ", value)
            elif key == "Customer":
                print("\t Customer Name: ", value[0])
                print("\t Customer Email: ", value[1])
                print("\t Customer Address: ", value[2])
            elif key == "Date":
                print("\t", key, ": ", value)
            elif key == "Estimate":
                print("\t", key, ": ", value)
            else:
                print("\t", key, " (", value[1] ,"): ", value[0]*value[1])
        print("\t**-------------------------**")
    print("**----------------------------------**")
    print()

def displayCurrentCart(cart):
    if cart == 0:
        print("Error: cart is empty.")
    else:
        print("**--------Current Cart--------**")
        for key in cart:
            print(key, ": ", cart[key][1])

def catelogDisplay(stock):
    print("**--------Available Stock--------**")
    print()
    for key in stock:
        print("**--------", key, "---------**")
        for letter, number in stock[key].items():
           print(letter, ": ", number)
           print()
    return 0

def getCustomerDetails():
    print()
    print("**---------Customer Details--------**")
    name = input("Enter Customer's name: ")
    email = input("Enter Customer's Email: ")
    address = input("Enter Customers address: ")
    customer = [name, email, address]
    return customer

def printShop(cart, estimate):
    fh = open("shopReceipt.txt", "w")
    fh.write("**--------Store Receipt--------**\n")
    for key in cart: 
        if key != "UID":
            if key != "Date":
                if key != "Customer":
                    if key != "Estimate":
                        if key != "19inch" and key != "23inch" and key != "2 Ports" and key != "4 Ports" and key != "Mini Tower" and key != "Midi Tower":
                            string = str(key) + ": \t\t\t" + str(cart[key][1]) + "\t\t" + str(cart[key][1]*cart[key][0])
                            fh.write(string)
                            fh.write("\n")
                        elif key == "Mini Tower" or key == "Midi Tower":
                            string = str(key) + ": \t" + str(cart[key][1]) + "\t\t" + str(cart[key][1]*cart[key][0])
                            fh.write(string)
                            fh.write("\n")
                        else:
                            string = str(key) + ": \t\t" + str(cart[key][1]) + "\t\t" + str(cart[key][1]*cart[key][0])
                            fh.write(string)
                            fh.write("\n")
        if key == "UID":
            string = "Order Reference Number: " + str(cart[key])
            fh.write(string)
            fh.write("\n")
            for key1 in cart:
                if key1 == "Date":
                    string = "Transaction Date: " + str(cart[key1])
                    fh.write(string)
                    fh.write("\n\n")
            string = ("**--------Item List--------**")
            fh.write(string)
            fh.write("\n")
            fh.write("Items\t\tAmount\t\tPrice\n")
       
        if key == "Customer":
            string = "\t\t\t+20% Labour Costs"
            fh.write(string)
            fh.write("\n")
            string = "Total: \t\t\t\t\t" + str(estimate)
            fh.write(string)
            fh.write("\n\n")
            fh.write("**---------Customer Details--------**\n")
            string = "Name: " + str(cart[key][0]) 
            fh.write(string)
            fh.write("\n")
            string = "Email: " + str(cart[key][1]) 
            fh.write(string)
            fh.write("\n")
            string = "Address: " + str(cart[key][2]) 
            fh.write(string)
            fh.write("\n")
    fh.write("**---------------------------------**")
    fh.close  

def printCustomer(cart, estimate):
    fh = open("customerReceipt.txt", "w")
    fh.write("**--------Store Receipt--------**\n")
    for key in cart: 
        if key != "UID":
            if key != "Date":
                if key != "Customer":
                    if key != "Estimate":
                        if key != "19inch" and key != "23inch" and key != "2 Ports" and key != "4 Ports" and key != "Mini Tower" and key != "Midi Tower":
                            string = str(key) + ": \t\t\t" + str(cart[key][1]) + "\t\t" + str(cart[key][1]*cart[key][0])
                            fh.write(string)
                            fh.write("\n")
                        elif key == "Mini Tower" or key == "Midi Tower":
                            string = str(key) + ": \t" + str(cart[key][1]) + "\t\t" + str(cart[key][1]*cart[key][0])
                            fh.write(string)
                            fh.write("\n")
                        else:
                            string = str(key) + ": \t\t" + str(cart[key][1]) + "\t\t" + str(cart[key][1]*cart[key][0])
                            fh.write(string)
                            fh.write("\n")
        if key == "UID":
            string = "Order Reference Number: " + str(cart[key])
            fh.write(string)
            fh.write("\n")
            for key1 in cart:
                if key1 == "Date":
                    string = "Transaction Date: " + str(cart[key1])
                    fh.write(string)
                    fh.write("\n\n")
            string = ("**--------Item List--------**")
            fh.write(string)
            fh.write("\n")
            fh.write("Items\t\tAmount\t\tPrice\n")
       
        if key == "Customer":
            string = "\t\t\t+20% Labour Costs"
            fh.write(string)
            fh.write("\n")
            string = "Total: \t\t\t\t\t" + str(estimate)
            fh.write(string)
            fh.write("\n\n")
            fh.write("**---------Customer Details--------**\n")
            string = "Name: " + str(cart[key][0]) 
            fh.write(string)
            fh.write("\n")
            string = "Email: " + str(cart[key][1]) 
            fh.write(string)
            fh.write("\n")
            string = "Address: " + str(cart[key][2]) 
            fh.write(string)
            fh.write("\n")
    fh.write("**---------------------------------**")
    fh.close  

def Main():
    stock = {'Processors': {'p3': 10, 'p5': 10, 'p7': 10}, 'RAM': {'16GB': 10, '32GB': 10}, 'Storage': {'1TB': 10, '2TB': 10}, 'Screen': {'19inch': 10, '23inch': 10}, 'Case': {'Mini Tower': 10, 'Midi Tower': 10}, 'USB Ports': {'2 Ports': 10, '4 Ports': 10}}
    inputUser=""
    estimateValue = 0
    orderNumbers = []
    todayDate = datetime.date.today()
    date = []
    date.append(todayDate)
    while inputUser != 'q' and inputUser != 'Q': #q or Q
        print()
        print("**--------Main Menu--------**")
        print("Option 1: Order Estimate") #Task 1
        print("Option 2: Place Order") #Task 2
        print("Option 3: Daily Order List") #Task 3
        print("Option 4: Catelog") #Task Display Stock Levels
        print("Option 5: Display Current Cart") #Display Cart
        print("Option 6: Delete Current Cart") #Remove Current cart
        print("Press q to Quit")
        print()
    
        inputUser = input("Enter the Option Number you wish to select: ")
        if inputUser == 'q' or inputUser == "Q":
            break
        elif int(inputUser) == 1:
            shoppingCart = createCart()
            estimateValue = estimate(shoppingCart)
            shoppingCart["Estimate"] = estimateValue
        elif int(inputUser) == 2:
            shoppingCart = checkCart(shoppingCart)
            if checkStock(shoppingCart, stock):
                stock = placeOrder(shoppingCart, stock, estimateValue, date)
                orderNumbers.append(shoppingCart)
                shoppingCart = 0
            else:
                print("Error: Insufficient Stock\n")
        elif int(inputUser) == 3:
            dailyOrderList(orderNumbers)
        elif int(inputUser) == 4:
            catelogDisplay(stock)
        elif int(inputUser) == 5:
            displayCurrentCart(shoppingCart)
        elif int(inputUser) == 6:
            if shoppingCart != 0:
                shoppingCart = 0
                print("Cart has been deleted")
                print()
            else:
                print("Cart is empty")
        elif inputUser != "q" and inputUser != "Q":
            print("Error: Enter a valid option number or q to quit")
            print("")
        
    return 0

Main()