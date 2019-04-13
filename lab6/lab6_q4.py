def format(num, width):
    # First find the number of digits
    digits = 0
    temp_num = num
    while temp_num > 0:  # Continue until temp_num is exhausted
        temp_num = temp_num // 10  # Divide by 10 and return quotient
        # 12345 // 10 = 1234, 1234 // 10 = 123, and so on
        digits += 1  # Add 1 to digits

    snum = str(num)  # Convert num into a string
    if width <= digits:
        # If the number of digits is less than the specified width,
        # just return the string value
        return snum
    else:
        # Otherwise find how much space is needed
        space = width - digits
        # Print '0' times however many spaces needed, concatenate snum
        snum = ('0' * space) + snum
        return snum


def main():
    unum = eval(input("Enter an integer: "))
    uwidth = eval(input("Enter width: "))
    print(format(unum, uwidth))

main()

'''
Enter an integer: 12345
Enter width: 1
12345

Enter an integer: 12345
Enter width: 5
12345

Enter an integer: 12345
Enter width: 7
0012345
'''
