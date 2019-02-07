amount = eval(input("Please Enter Investment Amount: "))
rate = eval(input("Please Enter Annual Interest Rate: "))
years = eval(input("Please Enter Number of Years: "))

mrate = rate / 1200
total = amount * (1 + mrate) ** (12 * years)

print("Accumulated Value is:", round(total, 2))

'''
Please Enter Investment Amount: 1000
Please Enter Annual Interest Rate: 4.25
Please Enter Number of Years: 1
Accumulated Value is: 1043.34
'''
