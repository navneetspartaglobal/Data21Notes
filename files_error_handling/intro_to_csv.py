import csv


def get_csv_file (csv_file):
    with open("user_details.csv") as csv_file:
        csvreader = csv.reader(csv_file, delimiter = ",")
        ans = list(csvreader)
    return ans


def transform_user_details(ans):
    new_list = []

    for row in ans:
        new_row = [row[1], row[2], row[3]]
        new_list.append(new_row)
    return new_list

def 