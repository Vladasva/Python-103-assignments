def enterMortgage():
    while True:
        try:
            mortgage = float(input("Please, enter your mortgage: "))
            if mortgage > 0:
                return mortgage
            else:
                print("The sum of mortgage cannot be 0 or negative.")
        except:
            print("Please, enter a number.")

def enterPeriods():
    while True:
        try:
            periods = int(input("Please, enter the number of periods: "))
            if periods > 0:
                return periods
            else:
                print("The number of periods cannot be 0 or negative.")
        except:
            print("Please, enter a number.")

def enterInterestRate():
    while True:
        try:
            interestRate = float(input("Please, enter interest rate: "))
            if interestRate > 0:
                return interestRate
            else:
                print("The interest rate cannot be 0 or negative.")
        except:
            print("Please, enter a number.")

def yearlyPayments():
    mortgage = enterMortgage()
    periods = enterPeriods()
    periods = float(periods)
    interestRate = enterInterestRate()
    yearlyInterestPayment = mortgage * (interestRate / 100)
    yearlyLoanPayment = mortgage / (periods/12)
    yearlyPayment = yearlyInterestPayment + yearlyLoanPayment
    yearlyPayment = round(yearlyPayment, 2)
    print(f"Your yearly payment is {yearlyPayment} EUR.")
    print(f'It will take {periods/12} years to pay all the mortgage. ')


def monthlyPayments():
    mortgage = enterMortgage()
    periods = enterPeriods()
    periods = float(periods)
    interestRate = enterInterestRate()
    monthlyInterestPayment = mortgage * ((interestRate/100)/12)
    monthlyLoanPayment = mortgage/periods
    monthlyPayment = monthlyInterestPayment + monthlyLoanPayment
    monthlyPayment = round(monthlyPayment, 2)
    print(f"Your monthly payment is {monthlyPayment} EUR.")
    print(f'It will take {periods} months to pay all the mortgage. ')

def dailyPayments():
    mortgage = enterMortgage()
    periods = enterPeriods()
    periods = float(periods)
    interestRate = enterInterestRate()
    dailyInterestPayment = mortgage * ((interestRate / 100) / 365)
    dailyLoanPayment = mortgage / ((periods/12) * 365)
    dailyPayment = dailyInterestPayment + dailyLoanPayment
    dailyPayment = round(dailyPayment, 2)
    print(f"Your daily payment is {dailyPayment} EUR.")
    print(f'It will take {((periods/12) * 365)} days to pay all the mortgage. ')

def paymentsOptions():
    while True:
        options = input("Please, enter 'daily,' 'monthly,' or 'yearly' to see loan payment by day, month or year. ").lower()
        try:
            if options == 'daily':
                dailyPayments()
                break
            elif options == 'monthly':
                monthlyPayments()
                break
            elif options == 'yearly':
                yearlyPayments()
                break
        except:
            print('Not valid option!')

paymentsOptions()





