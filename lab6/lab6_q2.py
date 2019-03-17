def print_chars(ch1, ch2, num_per_line):
    a = ord(ch1) # Get the decimal value of ch1 (1 = 49 in ASCii)
    b = ord(ch2) # Get the decimal value of ch2 (Z = 90 in ASCii)
    c = (b - a) + 1 # Find the difference between a and b,
                    # so we know how many times to run the loop
                    # 49 - 90 = 41, if we don't add 1 it will stop at 'Y'
    y = 1 # Counter to keep track

    while y <= c:
        if y % num_per_line == 0:
            # If y divides into num_per_line evenly, print on a new line,
            # this will happen N(th) time depending on the argument given
            print(chr(a))
        else:
            # Otherwise print on the same line with a space
            print(chr(a), end = " ")
        # Add 1 to 'a', this will represent the next value on the ASCii table
        a += 1
        # Increase counter by 1
        y += 1

def main():
    print_chars("1", "Z", 10)

main()

'''
1 2 3 4 5 6 7 8 9 :
; < = > ? @ A B C D
E F G H I J K L M N
O P Q R S T U V W X
Y Z
'''
