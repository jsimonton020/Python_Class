def print_chars(ch1, ch2, num_per_line):
    d_ch1 = ord(ch1) # Get the decimal value of ch1 (1 = 49 in ASCii)
    d_ch2 = ord(ch2) # Get the decimal value of ch2 (Z = 90 in ASCii)
    y = 1 # Counter to keep track

    while y <= (d_ch2 - d_ch1) + 1:
        if y % num_per_line == 0:
            # If y divides into num_per_line evenly, print on a new line,
            # this will happen N(th) time depending on the argument given
            print(chr(d_ch1))
        else:
            # Otherwise print on the same line with a space
            print(chr(d_ch1), end = "")
        # Add 1 to d_ch1, this will represent the next value on the ASCii table
        d_ch1 += 1
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
