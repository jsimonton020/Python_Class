def is_passwd(passwd):
    digits = 0
    for char in passwd:
        if char.isdigit() is True:
            digits += 1
        elif char.isalpha() is False:
            return False
    if len(passwd) < 8 or digits < 2:
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
