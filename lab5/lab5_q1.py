pos = 0
neg = 0
tot = 0
count = 0

num = eval(input("Enter an integer, the input ends if it is 0: "))

while True:
    if num > 0:
        pos += 1
        count += 1
        tot += num
    elif num <0:
        neg += 1
        count += 1
        tot += num
    elif num == 0:
        print("Exiting.")
        break
    num = eval(input("Enter an integer, the input sends if it is 0: "))

# This is to prevent dividing my 0
if count > 0:
    avg = tot / count
    print("\nThe number of positives is", pos)
    print("The number of negatives is", neg)
    print("The total is", tot)
    print("The average is", format(avg, ".2f"))
elif count == 0:
    print("You did not enter anything.")

'''
Enter an integer, the input ends if it is 0: 1
Enter an integer, the input sends if it is 0: 2
Enter an integer, the input sends if it is 0: -1
Enter an integer, the input sends if it is 0: 3
Enter an integer, the input sends if it is 0: 0

Exiting.

The number of positives is 3
The number of negatives is 1
The total is 5
The average is 1.25

Enter an integer, the input ends if it is 0: 0
Exiting.
You did not enter anything.
'''
