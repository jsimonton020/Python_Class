def is_passwd(passwd):
    if len(passwd) < 8: # if passwd it not 8 characters passwd is not valid
        return False
    digits = 0 # set counter to 0
    for char in passwd: # iterate over every character in the string
        if char.isdigit() is True:
            digits += 1 # if you find a digit add 1 to counter
        elif char.isalpha() is False:
            # if you find anything other than an alpha character passwd is not valid
            return False
    if digits < 2: # if you found less than 2 digits passwd is not valid
        return False
    else:
        return True


def main():
    passwd = input("Enter password: ")
    if is_passwd(passwd) is True:
        print("Valid password")
    else:
        print("Invalid password")

main()

'''
Enter password: passw0rd1
Valid password

Enter password: password1
Invalid password

Enter password: passwd
Invalid password

Enter password: passw0rd1!
Invalid password
'''
