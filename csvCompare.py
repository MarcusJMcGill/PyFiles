from csv_diff import load_csv, compare
import pprint
import csv

roster = input("Enter path to main csv file: ")
export = input("Enter path to comparative csv file: ")

# Saves the comparison data from the designated .csv files in a dictionary
diff = compare(
    load_csv(open(roster.strip()), key="ID"),
    load_csv(open(export.strip()), key="ID")
)
added = diff['added']
removed = diff['removed']
pprint.pprint(diff)
# pprint.pprint(added)
# pprint.pprint(removed)
print()

with open('/Users/laptop/Desktop/MissingFromRoster.csv', 'w') as file:
    csvWriter = csv.writer(file)

    # Writing the file header
    numOfStudentKeys = len(added[0].keys())
    studentKeys = list(added[0].keys())
    csvWriter.writerow(studentKeys)
    print(('*' * 20) + '\n' + str(len(added)) + " " + 'Missing From the Roster' + '\n')
    print(('*' * 20))

    # Writing student data to file
    for student in added:
        studentsValues = list(student.values())
        print(studentsValues)
        csvWriter.writerow(studentsValues)
    print(('*' * 20) + '\n')

with open('/Users/laptop/Desktop/MissingFromPS.csv', 'w') as file:
    print(('*' * 20) + '\n' + str(len(removed)) + " " + 'Missing From the Powerschool')
    print(('*' * 20))
    csvWriter = csv.writer(file)

    # Writing the file header
    numOfStudentKeys = len(added[0].keys())
    studentKeys = list(added[0].keys())
    csvWriter.writerow(studentKeys)

    # Writing student data to file
    for student in removed:
        studentsValues = list(student.values())
        print(studentsValues)
        csvWriter.writerow(studentsValues)
    print(('*' * 20) + '\n')

