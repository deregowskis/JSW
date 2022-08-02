new_list = []
with open('/Desktop/work/jsw/export_equal_sets.jsonl') as f:
    i = 0
    for line in f:
        new_line = str(line)
        if new_line.startswith('#{"imageGcsUri":'):
            new_line = new_line.replace('#{"imageGcsUri":','{"imageGcsUri":')
            if i%2 != 0:
                new_line = new_line.replace('"dataItemResourceLabels":{'+'}','"dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "validation"}')
            else:
                new_line = new_line.replace('"dataItemResourceLabels":{'+'}','"dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "test"}')
            #testowy
        else:
            new_line = new_line.replace('"dataItemResourceLabels":{'+'}','"dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "training"}')
        new_list.append(new_line)
        i=i+1

with open('/Desktop/work/jsw/manual_split.jsonl','w') as f:
    for element in new_list:
        f.write(element)