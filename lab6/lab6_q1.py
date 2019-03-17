def reverse(num):
    r = 0 # Set r to 0
    while num > 0: # Continue until num is exhuasted
        y = num % 10 # Take the last digit of num, store in y
        # Add y to r * 10
        # Ex. 54 * 10 = 540, add 'y' will be 54y
        r = (r * 10) + y
        num = num // 10 # Take the remaining digits in num
    return r # Return the reversed order

def main():
    num = eval(input("Please enter and integer: "))
    print(reverse(num))

main()

'''
Please enter and integer: 12345
54321

Please enter and integer: 987654321
123456789
'''
