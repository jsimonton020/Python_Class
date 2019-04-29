def sum_column(m, col_index):
    total = 0 # Set total to 0
    for row in range(len(m)): # Count element in matrix, iterate that many times
        total += matrix[row][col_index] # Find element by list index, add to total
    return total

matrix = [] # Create empty list
for row in range(3): # Do this 3 times
    # Take input from the user, and put in a list
    choice = input("Enter a 3-by-4 matrix row for row " + str(row) + ": ").split()
    # Convert the elements to integers using list comprehension
    i = [eval(x) for x in choice]
    # Append the list to matrix
    matrix.append(i)

print("\nSum of the elements for column 0 is", sum_column(matrix, 0))
print("Sum of the elements for column 1 is", sum_column(matrix, 1))
print("Sum of the elements for column 2 is", sum_column(matrix, 2))
print("Sum of the elements for column 3 is", sum_column(matrix, 3))


'''
Enter a 3-by-4 matrix row for row 0: 1.5 2 3 4
Enter a 3-by-4 matrix row for row 1: 5.5 6 7 8
Enter a 3-by-4 matrix row for row 2: 9.5 1 3 1

Sum of the elements for column 0 is 16.5
Sum of the elements for column 1 is 9
Sum of the elements for column 2 is 13
Sum of the elements for column 3 is 13
'''
