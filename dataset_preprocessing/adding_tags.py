new_list = []
with open('jsw/enriched/enriched_1435.jsonl') as f:
    i = 0
    for line in f:
        new_line = str(line)
        # select 20 percent of the whole dataset
        if new_line.startswith('#{"imageGcsUri":'):
            new_line = new_line.replace('#{"imageGcsUri":','{"imageGcsUri":')
            # 20 percent -> 10 percent + 10 percent
            if i%2 != 0:
                new_line = new_line.replace('"dataItemResourceLabels":{'+'}','"dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "validation"}')
            else:
                new_line = new_line.replace('"dataItemResourceLabels":{'+'}','"dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "test"}')
            #testowy
        # select 80 percent of the whole dataset as the training dataset
        else:
            new_line = new_line.replace('"dataItemResourceLabels":{'+'}','"dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "training"}')
        new_list.append(new_line)
        i=i+1

with open('/jsw/enriched/enriched_1435_splitted.jsonl','w') as f:
    for element in new_list:
        f.write(element)