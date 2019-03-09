num1 = eval(input("Enter number 1: "))
num2 = eval(input("Enter number 2: "))
num3 = eval(input("Enter number 3: "))

if num1 > num2 > num3:
    print(num3, num2, num1)
elif num1 > num3 > num2 :
    print(num2, num3, num1)
elif num2 > num1 > num3:
    print(num3, num1, num2)
elif num2 > num3 > num1:
    print(num1, num3, num2)
elif num3 > num1 > num2:
    print(num2, num1, num3)
elif num3 > num2 > num1:
    print(num1, num2, num3)

'''
Enter number 1: 1
Enter number 2: 2
Enter number 3: 3
1 2 3

Enter number 1: 3
Enter number 2: 2
Enter number 3: 1
1 2 3

Enter number 1: 123
Enter number 2: 456
Enter number 3: 789
123 456 789

Enter number 1: 987
Enter number 2: 654
Enter number 3: 321
321 654 987
'''
