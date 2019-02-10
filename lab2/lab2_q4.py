pounds = eval(input("Please enter weight in pounds: "))
height = eval(input("Please enter height in inches: "))

mpounds = pounds * 0.45359237
mheight = height * 0.0254

print("BMI is", round(mpounds / mheight**2, 4))

'''
Please enter weight in pounds: 95.5
Please enter height in inches: 50
BMI is 26.8573
'''
