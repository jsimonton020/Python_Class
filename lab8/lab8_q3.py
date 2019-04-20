def reverse(s):
    rstring = ""
    for chr in s:
        rstring = chr + rstring
    return rstring

def main():
    print(reverse(input("Enter a string: ")))

main()
