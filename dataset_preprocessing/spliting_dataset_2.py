import random

dataset_enriched = []
dataset_org = []
with open('jsw/enriched/enriched_1716.jsonl') as f:
    for line in f:
        dataset_enriched.append(line)
print("whole enriched dataset size: ", len(dataset_enriched))
#
with open('jsw/export/export.jsonl') as f:
    for line in f:
        dataset_org.append(line)
print("whole org dataset size: ", len(dataset_org))


cut = 0.2 * len(dataset_org)
test_validation_set = random.sample(dataset_org, round(cut))
test_set = []
validation_set = []
print("test_validation_set size: ", len(test_validation_set))
cut = 0.5 * len(test_validation_set)
test_set = random.sample(test_validation_set, round(cut))
print("test set size: ", len(test_set))
for value in test_validation_set:
    if value not in test_set:
        validation_set.append(value)
print("validation set size: ", len(validation_set))

# train_set = [value for value in dataset_enriched if value not in (test_set or validation_set)]
train_set = []
for value in dataset_org:
    if value not in test_validation_set:
        train_set.append(value)
print("train size: ", len(train_set))

final_train_set = []
for i in range(len(train_set)):
    tmp = train_set[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","', 1)[0]
    tmp = tmp.split(".")[0]
    tmp = '/' + tmp
    tmp2 = tmp + '.'
    tmp = tmp + '_'
    # print(tmp)
    with open('jsw/enriched/enriched_1716.jsonl') as f:
        for line in f:
            if line.find(tmp) != -1 or line.find(tmp2) != -1:
                final_train_set.append(line)
print("final train set size: ", len(final_train_set))

with open('jsw/split/v2_enriched_1716_training.jsonl', 'w') as f:
    j = 0
    num_urobkowy = 0
    num_obudowa = 0
    for i in range(len(final_train_set)):
        if final_train_set[i].find('urobkowy') != -1:
            if j < len(train_set):
                if num_urobkowy < 70:
                    if final_train_set[i].find('KOb_kontenerObudowa') != -1:
                        if num_obudowa < 70:
                            f.write(final_train_set[i])
                            j = j+1
                            num_urobkowy += 1
                            num_obudowa += 1
                    else:
                        f.write(final_train_set[i])
                        j = j + 1
                        num_urobkowy += 1
                elif final_train_set[i].find('KOb_kontenerObudowa') != -1:
                    if num_obudowa < 70:
                        f.write(final_train_set[i])
                        j = j + 1
                        num_obudowa += 1
        elif final_train_set[i].find('KOb_kontenerObudowa') != -1:
            if num_obudowa < 70:
                f.write(final_train_set[i])
                j = j + 1
                num_obudowa += 1
        else:
            if j < len(train_set):
                f.write(final_train_set[i])
                j = j+1
#
with open('jsw/split/v2_tmp_enriched_1716_training.jsonl', 'w') as f:
    for i in range(len(train_set)):
        f.write(train_set[i])

with open('jsw/split/v2_enriched_1716_validation.jsonl', 'w') as f:
    for i in range(len(validation_set)):
        f.write(validation_set[i])

with open('jsw/split/v2_enriched_1716_testing.jsonl', 'w') as f:
    for i in range(len(test_set)):
        f.write(test_set[i])
