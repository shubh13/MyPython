import csv

data = [[1, 2, 3, 4], [0.1, 0.2, 0.3, 0.4]]

dictdata = {
    "integers" : [1, 2, 3, 4],
    "decimals" : [0.1, 0.2, 0.3, 0.4]
}

with open("data.csv") as datafile:
    reader = csv.reader(datafile)

    for values in reader:
        print(values)


class parent():
    def childfun(self):
        print("I am a child function of a parent class")

class child(parent):
    parent.childfun()

