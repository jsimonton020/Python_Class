def reverse(s):
    string = ""
    for i in s:
        s2 = s[:-1]
        string += s2
    print(string)


def main():
    s = input("Enter string: ")
    reverse(s)

main()
