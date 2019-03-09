import random

num1 = random.randint(1, 99)
num2 = random.randint(1, 99)

answer = eval(input("What is " + str(num1)  +" + " + str(num2) + "? "))

print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)

'''
What is 99 + 62? 161
99 + 62 = 161 is True


What is 46 + 11? 50
46 + 11 = 50 is False
'''
