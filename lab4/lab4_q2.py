print("Months: Jan=1, Feb=2, Mar=3, etc.")
month = eval(input("Enter month: "))
year = eval(input("Enter year: "))

if month == 1:
    pmonth = "January"
if month == 2:
    pmonth = "February"
if month == 3:
    pmonth = "March"
if month == 4:
    pmonth = "April"
if month == 5:
    pmonth = "May"
if month == 6:
    pmonth = "June"
if month == 7:
    pmonth = "July"
if month == 8:
    pmonth = "August"
if month == 9:
    pmonth = "September"
if month == 10:
    pmonth = "October"
if month == 11:
    pmonth = "November"
if month == 12:
    pmonth = "December"

if month == 1 or month ==  3 or month == 5 or month == 7 \
or month == 8 or month == 10 or month == 12:
    print("\n", pmonth, year, "has 31 days" )
elif month !=2:
    print("\n", pmonth, year, "has 30 days" )
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("\nThis is a leap year")
    print(pmonth, year, "has 29 days")
else:
    print("\n", pmonth, year, "has 28 days")

'''
Months: Jan=1, Feb=2, Mar=3, etc.
Enter month: 2
Enter year: 2000

This is a leap year
February 2000 has 29 days


Months: Jan=1, Feb=2, Mar=3, etc.
Enter month: 3
Enter year: 2005

 March 2005 has 31 days


Months: Jan=1, Feb=2, Mar=3, etc.
Enter month: 4
Enter year: 1998

 April 1998 has 30 days
'''
