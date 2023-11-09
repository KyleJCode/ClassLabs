def hex_char_decode(digit):
    letter_dict = {'A': 10,
                   'B': 11,
                   'C': 12,
                   'D': 13,
                   'E': 14,
                   'F': 15
                   }
    if str(digit.upper()) in letter_dict:   # Checks if a letter is present in the dict and returns its value if so
        return int(letter_dict[digit.upper()])
    else:
        try:
            return int(digit)
        except ValueError:
            return digit
def hex_string_decode(hex):
    letter_dict = {'A': 10,
                   'B': 11,
                   'C': 12,
                   'D': 13,
                   'E': 14,
                   'F': 15
                   }
    j = len(hex) - 1
    num = 0
    for i in range(len(hex)):
        placeholder = 0
        if str(hex[i].upper()) in letter_dict:
            placeholder = letter_dict[hex[i].upper()]  # Converts a given letter into its number value
        else:
            try:
                placeholder = int(hex[i])
            except ValueError:
                print("ERROR")
        num += (placeholder*(pow(16, j)))  # Adds the value of placeholder into the sum to be returned
        j -= 1
    return num

def binary_string_decode(binary):
    count = len(binary)
    if count >= 10:
        num = 0
        if binary[1] == 'b':
            newnewbinary = binary[2:]
            j = len(newnewbinary)
        elif binary[1] != 'b':
            newnewbinary = binary[0:]
            j = len(newnewbinary)
    elif count < 10 and binary[1] == 'b':
        newbinary = binary[2:]
        zeros_to_fill = (8 - len(newbinary)) + len(newbinary)
        newnewbinary = newbinary.zfill(zeros_to_fill)
        num = 0
        j = len(newnewbinary)
    elif count < 10 and binary[1] != 'b':
        zeros_to_fill = (8 - len(binary))+len(binary)
        newbinary = binary.zfill(zeros_to_fill)
        num = 0
        j = len(newbinary)
        newnewbinary = newbinary
    for i in range(0, len(newnewbinary), 1):
        j -= 1
        num += (int(newnewbinary[i]) * (pow(2, j)))  # Decodes binary and adds up its parts
    return num

def binary_to_hex(binary):
    integer_to_convert = binary_string_decode(binary)
    list_of_nums = []
    i = -1
    letter_dict = {10: 'A',
                   11: 'B',
                   12: 'C',
                   13: 'D',
                   14: 'E',
                   15: 'F'
                   }
    while integer_to_convert > 0:
        i += 1
        list_of_nums.append((integer_to_convert % 16))
        if list_of_nums[i] in letter_dict.keys():
            list_of_nums.append(letter_dict[list_of_nums[i]])  # Converts binary to hexadecimal using integers
            list_of_nums.remove(list_of_nums[i])
        integer_to_convert = integer_to_convert//16
        string = ''.join(map(str, list_of_nums))
        string = string[::-1]
    return string

def main():
    option = 1
    while option != 4:
        result = 0
        print("Decoding Menu\n" + "-" * 13)
        print("1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n")
        option = int(input("Please enter an option: "))  # Displays menu and gives user input for menu choice selection
        if option == 1:
            num_string_char = input("Please enter the numeric string to convert: ")
            if '0x' in num_string_char:
                fixed_num_str = num_string_char[2::]
            else:
                fixed_num_str = num_string_char
            if len(fixed_num_str) == 1:
                digit = fixed_num_str
                result = hex_char_decode(digit)
                print(f"Result: {result}\n")
            else:
                hex = fixed_num_str
                print(f"Result: {hex_string_decode(hex)}\n")
        elif option == 2:
            binary = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_string_decode(binary)}\n")
        elif option == 3:
            binary = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_to_hex(binary)}\n")
    print("Goodbye!")


if __name__ == "__main__":
    main()
