import matplotlib.pyplot as plt
from collections import Counter
import csv

lines = []

with open('titanic_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        lines.append(line)
data = lines[1:]
passengers = []
headers = lines[0]

for d in data:
    p = {}
    for i in range(0,len(headers)):
        key = headers[i]
        value = d[i]
        p[key] = value
    passengers.append(p)
survived = [p['Survived'] for p in passengers]
pclass = [p['Pclass'] for p in passengers]
age = [float(p['Age']) for p in passengers if p['Age'] != '']
gender_survived = [p['Sex'] for p in passengers if int(p['Survived']) == 1]

plt.title("Survival Status")
plt.pie(Counter(survived).values(), labels=["Did Not Survive", "Survived"], autopct='%1.1f%%', 
        colors=['lightblue', 'lightgreen'])
plt.show()

plt.title("Surviving Passengers Count by Gender")
plt.bar(["Female", "Male"], Counter(gender_survived).values(), tick_label=["Female", "Male"])
plt.show()