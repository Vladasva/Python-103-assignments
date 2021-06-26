def enterPrice():
    while True:
        try:
            price = float(input("Please enter a price:"))
            if price > 0:
                return price
                break
            else:
                print("The price cannot be 0 or negative.")
        except:
            print("Please, enter a number")

def enterTaleHeight():
    while True:
        try:
            taleHeight = float(input("Please enter tale's height in cm:"))
            if taleHeight > 0:
                return taleHeight
                break
            else:
                print("The height cannot be 0 or negative.")
        except:
            print("Please, enter a number")

def enterTaleWidth():
    while True:
        try:
            taleWidth = float(input("Please enter tale's width in cm:"))
            if taleWidth > 0:
                return taleWidth
                break
            else:
                print("The width cannot be 0 or negative.")
        except:
            print("Please, enter a number")

def enterFloorHeight():
    while True:
        try:
            floortHeigth = float(input("Please enter floor height in meters:"))
            if floortHeigth > 0:
                return floortHeigth
                break
            else:
                print("The height cannot be 0 or negative.")
        except:
            print("Please, enter a number")

def enterFloorWidth():
    while True:
        try:
            floorWidth = float(input("Please floor width in meters:"))
            if floorWidth > 0:
                return floorWidth
                break
            else:
                print("The width cannot be 0 or negative.")
        except:
            print("Please, enter a number")

def execution():
    totalPrice = 0.00
    tale = (enterTaleHeight() * enterTaleWidth())/100
    floor = enterFloorHeight() * enterFloorWidth()
    numberTales = floor / tale
    numberTales = float(numberTales)
    totalPrice = numberTales * enterPrice()
    totalPrice = round(totalPrice, 2)
    print(f"You will need {numberTales} for the floor.")
    print(f"You will need plates for {totalPrice} Euro.")

execution()


