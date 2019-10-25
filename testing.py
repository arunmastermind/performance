import json
import pprint
import pandas as pd
import csv
# with open('regressions.json', 'r') as f:
#     data = f.read()
#     json_data = json.loads(data)
# df = pd.read_json('regressions.json')
# df = pd.json_normalize(json.dumps(json_data))
# df = pd.read_json(json.dumps(json_data), orient='records').T

with open('regressions.json', 'r') as f:
    data = json.load(f)
# print(data)
benchmark = builds = []

higher_better = []
lower_better = []
x = ""
myfile2 = open('lower.csv', 'w')
myfile1 = open('higher.csv', 'w')
# writer1 = csv.writer(myfile1)
writer2 = csv.writer(myfile2)
for i in data:
    closeScores = ([list(a.values()) for a in i.values()])
    for i in closeScores[0]:
        aa = (list(i[0].values())[0][0]) + "\n"
        print(aa)
        if (list(i[0].values())[0][1]) == 'higher_better':
            higher_better.append(list(i[0].values())[0][0])
            myfile1.write(aa)
            # myfile1.write(list(i[0].values())[0][0])
            # print((list(i[0].values())[0][0]))
            # writer1.writerow(aa)
        else:
            lower_better.append(list(i[0].values())[0][0])
            # myfile2.writerow((list(i[0].values())[0][0]))
            writer2.writerow((list(i[0].values())[0][0]))

myfile2.close()
myfile1.close()
# print(f'H : {higher_better}')
# print(f'L : {lower_better}')

#
df = pd.read_csv('higher.csv')
print(df.head(10))