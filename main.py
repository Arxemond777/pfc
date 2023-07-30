import csv

input_data = """
05+03+05+03=16+035=195+03+034=26+04=3+05=35+05=4
45+18+45=108+44=152+18=170+30=200
400+150+400=950+350=1300+150=1450+350=1800

05+15=2+05=25+06=311
400+400=800+350=1150+350=1500
45+45=90+26=116+26=142

05+15=2+05=25+06=3.1
45+45=90+26=116+26=142
400+400=800+350=1150+350=1501
"""

data = []
lines = input_data.strip().split("\n")

i = 0
row = {}
for line in lines:
    if i == 0: # water
        water = str(line.split("=")[-1].strip())
        if (len(water) > 1 and water[1] != "."): # if 41->4.1 but don't touch 3.1
            water = water[:1] + "." + water[1:]
        row["water"] = water
    elif i == 1 or i == 2:
        calories_or_protein = str(line.split("=")[-1].strip())
        if len(calories_or_protein) == 4 and "calories" not in row:
            calories = calories_or_protein
            row["calories"] = calories
        elif len(calories_or_protein) == 3 and "protein" not in row:
            protein = calories_or_protein
            row["protein"] = protein
        else:
            print(line, " ", row)
            raise Exception("aaaaa")

    i += 1
    if i == 3:
        data.append(row)

    if i >= 4:
        i = 0
        row = {}

# print(data)

# Extract the fieldnames from the first dictionary
fieldnames = data[0].keys()

# Write the data to the CSV file
with open("output.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write the data rows