def enterCost():
    while True:
        try:
            cost = float(input("Please enter the cost: "))
            if cost > 0:
                return cost
            else:
                print("Cost cannot be 0 or negative number!")
        except:
            print("Please enter a number!")

def moneyGiven():
    while True:
        try:
            money = float(input("Please enter the money given: "))
            if money > 0:
                return money
            else:
                print("Sum cannot be 0 or negative number!")
        except:
            print("Please enter a number!")

def changeReturn():
    cost = enterCost()
    money = moneyGiven()
    difference = 0.0
    difference = money - cost

    if difference == 0.0:
        print("No change")
    elif difference > 0:
        if difference >= 200:
            twoHundreds = difference / 200
            twoHundreds = int(twoHundreds)
            print(f"Give a change {twoHundreds} in 200 EUR")
            difference = difference - (twoHundreds * 200)
        if 100 <= difference < 200:
            hundreds = difference / 100
            hundreds = int(hundreds)
            print(f"Give a change {hundreds} in 100 EUR")
            difference = difference - (hundreds * 100)
        if difference >= 50 < 100:
            fifties = difference / 50
            fifties = int(fifties)
            print(f"Give a change {fifties} in 50 EUR")
            difference = difference - (fifties * 50)
        if difference >= 20 < 50:
            twenties = difference / 20
            twenties = int(twenties)
            print(f"Give a change {twenties} in 20 EUR")
            difference = difference - (twenties * 20)
        if difference >= 10 < 20:
            tens = difference / 10
            tens = int(tens)
            print(f"Give a change {tens} in 10 EUR")
            difference = difference - (tens * 10)
        if difference >= 5 < 10:
            fives = difference / 5
            fives = int(fives)
            print(f"Give a change {fives} in 5 EUR")
            difference = difference - (fives * 5)
        if difference >= 2 < 5:
            twos = difference / 2
            twos = int(twos)
            print(f"Give a change {twos} in 2 EUR")
            difference = difference - (twos * 2)
        if difference >= 1 < 2:
            ones = difference / 1
            ones = int(ones)
            print(f"Give a change {ones} in 1 EUR")
            difference = difference - (ones * 1)
        if difference >= 0.5 < 1:
            fiftyCnt = difference / 0.5
            fiftyCnt = int(fiftyCnt)
            print(f"Give a change {fiftyCnt} in 0.5 EUR")
            difference = difference - (fiftyCnt * 0.5)
        if difference >= 0.2 < 0.5:
            twentyCnt = difference / 0.2
            twentyCnt = int(twentyCnt)
            print(f"Give a change {twentyCnt} in 0.2 EUR")
            difference = difference - (twentyCnt * 0.2)
        if difference >= 0.1 < 0.2:
            tenCnt = difference / 0.1
            tenCnt = int(tenCnt)
            print(f"Give a change {tenCnt} in 0.1 EUR")
            difference = difference - (tenCnt * 0.1)
        if difference >= 0.05 < 0.1:
            fiveCnt = difference / 0.05
            fiveCnt = int(fiveCnt)
            print(f"Give a change {fiveCnt} in 0.05 EUR")
            difference = difference - (fiveCnt * 0.05)
        if difference >= 0.02 < 0.05:
            twoCnt = difference / 0.02
            twoCnt = int(twoCnt)
            print(f"Give a change {twoCnt} in 0.02 EUR")
            difference = difference - (twoCnt * 0.02)
        if difference >= 0.01 < 0.02:
            oneCnt = difference / 0.01
            oneCnt = int(oneCnt)
            print(f"Give a change {oneCnt} in 0.01 EUR")
            difference = difference - (oneCnt * 0.01)

    elif difference < 0:
        print("Cost cannot be bigger when money given!")


changeReturn()
