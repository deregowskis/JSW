i=0

validation = []
test = []

with open('/Desktop/work/jsw/to_split.jsonl') as f:
    for line in f:
        if i%2==0:
            validation.append(line)
        else:
            test.append(line)
        i=i+1

print(len(test))
print(len(validation))
with open('/Desktop/work/jsw/new_test.jsonl','w') as f:
    for element in test:
        f.write(element)

with open('/Desktop/work/jsw/new_validation.jsonl','w') as f:
    for element in validation:
        f.write(element)