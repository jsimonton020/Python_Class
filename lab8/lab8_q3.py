def reverse(s):
    rstring = "" # make a new empty rstring
    for chr in s: # iterate over every character in original string
        rstring = chr + rstring # concatenate character to end of rstring
    return rstring

def main():
    print(reverse(input("Enter a string: ")))

main()

'''
Enter a string: This is a String
gnirtS a si sihT

Enter a string: WasItARatISaw
waSItaRAtIsaW
'''
