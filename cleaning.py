import numpy as np
import pandas as pd
import csv

csvFile = open('weatherHistory.csv', "r")
reader = csv.reader(csvFile)

i = 0
res = []
for item in reader:
    i+=1
    # ignore the first line
    # if reader.line_num == 1:
    #     continue
    isZero = False
    for x in item:
        # print(type(x))
        if x == "0":
            isZero = True
            
            break
    if isZero == False:
        res.append(item)
    # if i == 2:
    #     break

csvFile.close()

# output csv file after cleaning
csv_label1 = open("clean.csv", "w")
writer_label = csv.writer(csv_label1)
i = 1
for x in res:
    writer_label.writerow(x)

csv_label1.close()

# data cleaning using pandas

# import numpy as np
# import pandas as pd

# df = pd.read_csv("weatherHistory.csv")
# name = 'Wind Bearing (degrees)'
# df["cleanBase"] = df[name]

# df = df[df.cleanBase!=0]
# # df = df[index]

# df.to_csv("cleanAfter.csv",index=False)