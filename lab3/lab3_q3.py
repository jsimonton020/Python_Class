name = input("Enter Employee's Name: ")
hours = eval(input("Enter Number of Hours Worked in a Week: "))
rate = eval(input("Enter Hourly Pay Rate: "))
fed = eval(input("Enter Federal Tax Withholding Rate: "))
state = eval(input("Enter State Tax Withholding Rate: "))
gross = rate * hours

print("Employee Name:", name)
print("Pay Rate:", rate)
print("Gross Pay:", format(gross, ".2f"))
print("Deductions:")
print("   Federal Withholding (20.0%):", format(gross * fed, ".2f"))
print("   State Withholding (9.0%):", format(gross * state, ".2f"))
print("   Total Deduction:", format((gross * fed) + (gross * state), ".2f"))
print("Net Pay:", format(gross - ((gross * fed) + (gross * state)), ".2f"))

'''
Enter Employee's Name: Bob
Enter Number of Hours Worked in a Week: 10
Enter Hourly Pay Rate: 9.75
Enter Federal Tax Withholding Rate: 0.20
Enter State Tax Withholding Rate: 0.09
Employee Name: Bob
Pay Rate: 9.75
Gross Pay: 97.50
Deductions:
   Federal Withholding (20.0%): 19.50
   State Withholding (9.0%): 8.78
   Total Deduction: 28.27
Net Pay: 69.22
'''
