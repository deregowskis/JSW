validation = []
test = []
training = []

with open('/Desktop/work/jsw/manual_split.jsonl') as f:
    for line in f:
        if line.count('{"aiplatform.googleapis.com/ml_use": "validation"}') != 0:
            validation.append(line)
        elif line.count('{"aiplatform.googleapis.com/ml_use": "test"}') != 0:
            test.append(line)
        else:
            training.append(line)

with open('/Desktop/work/jsw/validation','w') as f:
    for element in validation:
        f.write(element)

with open('/Desktop/work/jsw/test','w') as f:
    for element in test:
        f.write(element)

with open('/Desktop/work/jsw/training','w') as f:
    for element in training:
        f.write(element)