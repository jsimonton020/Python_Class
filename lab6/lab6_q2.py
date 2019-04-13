def print_chars(ch1, ch2, num_per_line):
    d_ch1 = ord(ch1)  # Get the decimal value of ch1
    d_ch2 = ord(ch2)  # Get the decimal value of ch2
    # range to know how many times to run the loop
    # counter to keep track of how many times the loop ran
    range = (d_ch2 - d_ch1) + 1
    counter = 1

    while counter <= range:
        if counter % num_per_line == 0:
            # If counter divides into num_per_line evenly, print on a new line
            # this will happen Nth time depending on the argument given
            print(chr(d_ch1))
        else:
            # Otherwise print on the same line with a space
            print(chr(d_ch1), end=" ")
        # Add 1, this will represent the next value on the ASCii table
        d_ch1 += 1
        # Increase counter by 1
        counter += 1


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
