def is_ssn():
    ssn = input("Enter SSN (ddd-dd-dddd): ")
    if len(ssn) == 11:
        if ssn.find("-") == 3 and ssn.rfind("-") == 6:
            if len(ssn[:3]) == 3 and len(ssn[4:6]) == 2 and len(ssn[7:11]) == 4:
                if ssn[:3].isdigit() and ssn[4:6].isdigit() and ssn[7:11].isdigit():
                    print("Valid SSN")
    else:
        print("Invalid SSN")


is_ssn()
