from console_gfx import ConsoleGfx
from collections import Counter
import math

def menu_display_and_option():
    print("\nRLE Menu\n--------")
    print("0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n", end="")
    print("5. Read Data Hax String\n6. Display Image\n7. Display HLE String\n8. Display Hex RLE Data"
          "\n9. Display Hex Flat Data")
    selection = int(input("\nSelect a Menu Option: "))
    return selection


def to_hex_string(data):
    hexa_letters = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f",
               }
    for i in range(len(data)):
        if data[i] in hexa_letters.keys():
            data[i] = str(hexa_letters[data[i]])
        string_return = ''.join(map(str, data))
    return string_return


def count_runs(flat_data):
    counter = 0
    p = 15
    z = math.ceil(len(flat_data)/15)
    for i in range(z):
        placeholder = flat_data[p-15:p]
        counter += len(set(placeholder))
        p += p
    print(counter)


def encode_rle(flat_data):
    nums_list = list(Counter(flat_data))[:]
    vals_list = list(Counter(flat_data).values())[:]
    print(vals_list[0])
    print(vals_list[1])
    






def get_decoded_length(rle_data):
    pass


def decode_rle(rle_data):
    pass


def string_to_data(data_string):
    manipulate_string = list(data_string)
    hexa_letters = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    for i in range(len(data_string)):
        if manipulate_string[i] in hexa_letters.keys():
            manipulate_string[i] = int(hexa_letters[manipulate_string[i]])
        else:
            manipulate_string[i] = int(manipulate_string[i])
    return manipulate_string


def main():
    choice = 1
    image_data = None
    print("Welcome to the RLE image encoder!")
    print("\nDisplaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    while choice != 0:
        choice = menu_display_and_option()
        if choice == 1:
            filename = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(filename)
        elif choice == 2:
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.\n")
        elif choice == 3:
            # RLEString = input("Enter an RLE string to be decoded: ")
            to_hex_string([3, 15, 6, 4])
        # elif choice == 4:
        #     HEXStringWithRLE = input("Enter the hex string holding RLE data: ")
        # elif choice == 5:
        #     HexStringWithFlat = input("Enter the hex string with flat data: ")
        elif choice == 6:
            ConsoleGfx.display_image(image_data)
        elif choice == 7:
            string_to_data("3f64")
        elif choice == 8:
            count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4])
        elif choice == 9:
            encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4])


if __name__ == '__main__':
    main()