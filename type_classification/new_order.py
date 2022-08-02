names = []
new_json = []
with open('/Desktop/work/jsw/new_training.jsonl') as f:
    for line in f:
        stripped = line.strip('{"imageGcsUri":"gs://wozy_jsw/augmentation').split('","',1)[0]
        stripped = stripped.strip('.png')[:-1][:-1]
        names.append(stripped)

with open('/Desktop/work/jsw/new_test.jsonl') as f:
    for line in f:
        stripped = line.strip('{"imageGcsUri":"gs://wozy_jsw/augmentation').split('","',1)[0]
        stripped = stripped.strip('.png')
        if stripped not in names:
            new_json.append(line)

with open('/Desktop/work/jsw/new_validation','w') as f:
    for element in new_json:
        f.write(element)
