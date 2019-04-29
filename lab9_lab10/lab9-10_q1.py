list1 = input("Enter integers between 1 and 100: ").split() # Get user input, and put is in a list
list2 = [] # Make an empty list
for i in list1: # Iterate over list1
    if i not in list2: # If the element is not in list2
        list2.append(i) # Add the element to list2 (so we don't have to count it again)
        count = list1.count(i) # Count the element in list1
        print(i, "occurs", count, "time" if count == 1 else "times") # Print the results



'''
Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2
2 occurs 2 times
5 occurs 2 times
6 occurs 1 time
4 occurs 1 time
3 occurs 1 time
23 occurs 1 time
43 occurs 1 time
'''
