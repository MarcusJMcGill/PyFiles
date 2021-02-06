from csv_diff import load_csv, compare
import pprint
import csv

path1 = input("Input the path of main .csv file: ")
path2 = input("Input the path of the second .csv file: ")

students1 = []
students2 = []

with open(path1.strip(), newline='') as file1:
    reader1 = csv.reader(file1)
    students1 = list(reader1)

with open(path2.strip(), newline='') as file2:
    reader2 = csv.reader(file2)
    students2 = list(reader2)

    keys = students1[0]
    students1 = [dict(zip(keys, student)) for student in students1]
    students2 = [dict(zip(keys, student)) for student in students2]

with open('/Users/laptop/Desktop/result.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()

    students1.pop(0)
    students2.pop(0)

    for student1 in students1:
        for student2 in students2:
            student1["Last Name"].strip()
            student2["Last Name"].strip()
            if student1["Last Name"] != student2["Last Name"] \
                    or student1["First Name"] != student2["First Name"]:
                print(student1["First Name"], " ", student1["Last Name"], "!=", student2["First Name"], " ", student2["Last Name"])

            if student1["Last Name"] == student2["Last Name"] \
                    and student1["First Name"] == student2["First Name"]:
                student1["ID"] = student2["ID"]
                student1["Birthdate"] = student2["Birthdate"]
        pprint.pprint(student1)
        writer.writerow(student1)
