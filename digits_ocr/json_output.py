# Requirement:
# Names of files match pattern "{name_of_truck}_{i}.png", i = 0,1,2,... (order of files within a truck is very important).

import argparse

# construct the argument parse and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", help = "path to the JSON file")
ap.add_argument("-b", "--bucket", help = "path to GCS bucket")
args = vars(ap.parse_args())

# read lines
lines = []
with open(args["file"]) as f:
    for line in f:
        lines.append(line)

# find prediction for each line
trucks = {}
for line in lines:
    start = line.find(args["bucket"]) + len(args["bucket"]) + 1
    end = line.find(".png")-2
    name = line[start:end]
    position = line[line.find(".png")-1]
    prediction = line[line.find('displayNames')+16]
    if name not in trucks:
        trucks[name]=[]
    trucks[name].append([position,prediction])

for key in trucks:
    number = ""
    for i in range(len(trucks[key])):
        for j in range(len(trucks[key])):
            if int(trucks[key][j][0]) == i:
                number += str(trucks[key][j][1])
    trucks[key]=number

print(trucks)