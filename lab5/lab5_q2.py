counter = 1 # Keep track of how many numbers get found
for num in range(100, 201):
    if (num % 5 == 0 and num % 6 != 0) or (num % 5 != 0 and num % 6 == 0):
        # Check if number is divisible by 5 or 6 but not both
        if counter % 10 == 0: # Every 10th time will print on a new line
            print(num)
        else:
            print(num, end = " ") # print with space
        counter += 1 # increase counter by one

'''
100 102 105 108 110 114 115 125 126 130
132 135 138 140 144 145 155 156 160 162
165 168 170 174 175 185 186 190 192 195
198 200
'''
