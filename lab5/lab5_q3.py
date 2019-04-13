# Get user input
num1 = eval(input("Enter integer 1: "))
num2 = eval(input("Enter integer 2: "))

# Find the smallest of the 2 numbers
d = min(num1, num2)

# Start from smallest of the two numbers and work your way down
while d >= 1:
    if num1 % d == 0 and num2 % d == 0:
        break # GCD found break from the loop
    d -= 1 # GCD not found, minus 1 from smallest number and keep going.
# Print results
print("GCD is", d)

'''
Enter integer 1: 8
Enter integer 2: 12
GCD is 4

Enter integer 1: 7
Enter integer 2: 13
GCD is 1
'''
