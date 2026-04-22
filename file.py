import csv 

# add data to a file

# data=[
#      ["Name", "Age", "City"],
#     ["Alice", 25, "New York"],
#     ["Bob", 30, "London"],
#     ["Charlie", 22, "Sydney"]
# ]

# with open("sure.csv" , 'w' , newline="") as file:
#     write = csv.writer(file)
#     write.writerows(data)
# print("Sucessfully created")

# Append newdata

# newdata=[
#     ["Satya" , 23 , "Dhenkanal"]
# ]

# with open("sure.csv" , 'a') as file:
#     write = csv.writer(file)
#     write.writerows(newdata)

# print("Append sucessfully")


#Read the file

with open("sure.csv" , 'r') as file:
    read = csv.reader(file)

    for row in read:
        print(row)

#read the file using dictreader

with open("sure.csv", mode="r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row["Name"], row["Age"], row["City"])