import csv


# def opening_file():
#     file_open = open("user_details.csv", "r")
#     return file_open

''' 
with open("user_details.csv", "r") as csvfile:
    #     csvreader = csv.reader(csvfile, delimiter=",")

'''

# Transformation


def transform_user_details(user_details):

    list_sample = []
    with open("user_details.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for item in csvreader:
            list_sample.append([item[1], item[2], item[-1]])
        return list_sample

#transform_user_details(user_details="user_details.csv")

# Loading the file after transformation: Loading

def create_csv_file(user_details, new_file_name):
    new_user_details = transform_user_details(user_details)
    print(new_user_details)
    transformed_list = []
    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details)

        for item in transformed_list:
            transformed_list.append([item[1], item[2], item[-1]])
            for item2 in new_file_name:
                print(item2)
        return new_file_name

    #print(new_file_name)


create_csv_file(user_details="user_details.csv", new_file_name="new_file.csv")

