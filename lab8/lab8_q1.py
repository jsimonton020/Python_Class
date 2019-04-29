def is_ssn():
    ssn = input("Enter SSN (ddd-dd-dddd): ")
    is_ssn_valid = False # set valid to False
    if len(ssn) == 11: # if ssn is not 11 characters ssn is not valid
         # if you don't find "-" in the right place ssn is not valid
        if ssn.find("-") == 3 and ssn.rfind("-") == 6:
            # if you don't find digits in the right place ssn is not vlaid
            if ssn[:3].isdigit() and ssn[4:6].isdigit() and ssn[7:11].isdigit():
                is_ssn_valid = True # set valid to True

    if is_ssn_valid == True:
        print('Valid SSN')
    else:
        print('Invalid SSN')


is_ssn()

'''
Enter SSN (ddd-dd-dddd): 123-45-6789
Valid SSN

Enter SSN (ddd-dd-dddd): 123-456-789
Invalid SSN
'''
