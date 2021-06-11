import csv

row = ["Apple", "Banana", "Cherry"]
data = ["Red", "Yellow", "Maroon"]

csv_file = open("data.csv", "w", newline='')

writeincsv = csv.writer(csv_file , quotechar='|', quoting=csv.QUOTE_MINIMAL)

writeincsv.writerow(row)
writeincsv.writerow(data)




