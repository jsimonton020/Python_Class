def sum_major_diagnal(m):
    total = 0 # Set total to 0
    for row in range(len(m)): # Count element in matrix, iterate that many times
        total += m[row][row] # Find element by list index, add to total
    return total


matrix = [] # Create empty list
for row in range(4): # Do this 4 times
    # Take input from the user, and put in a list
    choice = input("Enter a 4-by-4 matrix row for row " + str(row) + ": ").split()
    # Convert the elements to integers using list comprehension
    i = [eval(x) for x in choice]
    # Append the list to matrix
    matrix.append(i)

print("\nThe sum of elements in major diagnal is", sum_major_diagnal(matrix))

'''
Enter a 4-by-4 matrix row for row 0: 1 2 3 4
Enter a 4-by-4 matrix row for row 1: 5 6.5 7 8
Enter a 4-by-4 matrix row for row 2: 9 10 11 12
Enter a 4-by-4 matrix row for row 3: 13 14 15 16

The sum of elements in major diagnal is 34.5
'''
