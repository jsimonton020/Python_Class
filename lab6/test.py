input = eval(input(" "))
num = input
count = 0
while num > 0:
    num = num // 10
    count += 1

print('There are', count, "digits in", input)
