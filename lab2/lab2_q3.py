number = eval(input("Please enter a number between 0 and 1000: "))

last = number % 10
temp = number // 10
second = temp % 10
temp = temp // 10
third = temp

answer = last + second + third

print("The sum of the digits in", number, "is", answer)

'''
Please enter a number between 0 and 1000: 999
The sum of the digits in 999 is 27
'''
