import csv

itemName = input("Enter name of item (ex. Chromebook): ")
totalDevices = int(input("Enter total number of devices: "))
duplicates = int(input("Enter number of duplicates of each device: "))
filename = itemName + "_labels.csv"
deviceList = []

for i in range(totalDevices):
    currentDeviceNumber = i + 1
    for j in range(duplicates):
        numberOfLeadingZeros: int = len(str(totalDevices)) - len(str(currentDeviceNumber))
        leadingZeros = "0" * numberOfLeadingZeros
        currentDevice = [str(itemName) + "-" + leadingZeros + str(currentDeviceNumber)]
        print(str(itemName) + "-" + leadingZeros + str(currentDeviceNumber))
        deviceList += [currentDevice]

with open("/Users/laptop/Desktop/" + filename, 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerows(deviceList)

print()
print("*********FILE GENERATION SUCCESS*********")
print("File: ", filename, " located at /Users/laptop/Desktop/")
