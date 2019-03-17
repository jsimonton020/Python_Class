import random

def print_matrix(n):
    for rows in range(n): # First for loop are for rows, iterate 'n' times
        for columns in range(n): # Second for loop are for columns, iterate 'n' times
            # Print random 1 or 0 seperated by space
            print(random.randint(0, 1), end = " ")
        # Print a carriage return for a new row
        print("\r")

def main():
    n = eval(input("Enter n: "))
    print_matrix(n)

main()

'''
Enter n: 3
1 0 0
1 1 1
0 1 0

Enter n: 10
1 0 1 1 1 0 1 0 1 1
0 1 1 1 0 1 0 0 1 0
0 0 1 1 0 1 0 0 0 0
0 0 1 1 0 1 0 0 0 0
0 0 1 0 0 1 1 1 0 0
1 1 1 1 0 1 0 1 1 0
1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 0 1 0 1 0
1 0 1 1 0 0 0 1 0 0
1 0 1 0 1 1 0 1 1 1
'''
