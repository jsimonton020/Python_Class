list1 = input("Enter ten numbers: ").split() # Get user input, and put it in a list
list2 = [] # Make an empty list
for i in list1: # Iterate over list1
    if i not in list2: # If the element is not in list 2
        list2.append(i) # Add element to list 2
# Print out the distinct numbers on one line
print("The distinct numbers are: ", end=" ")
for i in list2:
    print(i, end=" ")


'''
Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
The distinct numbers are:  1 2 3 6 4 5

Enter ten numbers: 1 1 1 1 1 1 1 1 1 1
The distinct numbers are:  1
'''
