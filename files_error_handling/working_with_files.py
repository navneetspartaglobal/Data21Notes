def read_file(file):

    try:
        with open(file, "r") as opened_file:

        # open_file = open(file, "r")  # Open is a built-in function to open file
        # file_line_list = open_file.readlines()
        # print(file_line_list)
            for line in opened_file.readlines():
                print(line.rstrip('\n'))

        # open_file.close()

    except FileNotFoundError as errmsg:
        print("There has been an error opening your file")
        print(errmsg)

    finally:

        print("Execution complete")


#read_file("order.txt")


def write_to_file(item, file="order.txt"):
    try:

        with open(file, "a") as opened_file:  # this "W" will override the file and delete everything before writing
            for item in list_of_items:
                opened_file.write(item + "\n")

    except FileNotFoundError:
        print("file cannot be found")

    except FileExistsError:
        print("File already exist error")

items = input("Enter the items to include in order")
list_of_items = []
list_of_items.append(items)

write_to_file(list_of_items)
read_file("order.txt")