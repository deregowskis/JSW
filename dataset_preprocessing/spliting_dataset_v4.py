import random

dataset_enriched = []
dataset_org = []

# enriched_json_path = "/home/bilibala/Desktop/work/dataset/jsw/export_cropped_3003_org_aug.jsonl"
enriched_json_path = "/home/bilibala/Desktop/work/dataset/jsw/wozy_cropped_3003.jsonl"
org_json_path = "/home/bilibala/Desktop/work/dataset/jsw/wozy_cropped_3003.jsonl"

with open(f"{enriched_json_path}") as f:
    for line in f:
        dataset_enriched.append(line)
print("whole enriched dataset size: ", len(dataset_enriched))
#
with open(f"{org_json_path}") as f:
    for line in f:
        dataset_org.append(line)
print("whole org dataset size: ", len(dataset_org))

len_test_validation_set = 200
test_validation_set = []
test_set = []
validation_set = []

dataset_org = random.sample(dataset_org, len(dataset_org))
j = 0
num_urobkowy = 0
num_obudowa = 0
num_214_04 = 0
num_214_01 = 0
num_215_01 = 0
num_mater = 0
num_rzewiark = 0
for i in range(len(dataset_org)):
    if j < len_test_validation_set:
        if dataset_org[i].find('urobkow') != -1:
            if num_urobkowy < 28:
                test_validation_set.append(dataset_org[i])
                num_urobkowy += 1
                j += 1
        elif dataset_org[i].find('KOb_kontenerObudow') != -1:
            if num_obudowa < 28:
                test_validation_set.append(dataset_org[i])
                num_obudowa += 1
                j += 1
        elif dataset_org[i].find('JZR214_04') != -1:
            if num_214_04 < 28:
                test_validation_set.append(dataset_org[i])
                num_214_04 += 1
                j += 1
        elif dataset_org[i].find('JZR_214_01') != -1:
            if num_214_01 < 28:
                test_validation_set.append(dataset_org[i])
                num_214_01 += 1
                j += 1
        elif dataset_org[i].find('JZR_215_01') != -1:
            if num_215_01 < 28:
                test_validation_set.append(dataset_org[i])
                num_215_01 += 1
                j += 1
        elif dataset_org[i].find('KZ_kontenerMater') != -1:
            if num_mater < 28:
                test_validation_set.append(dataset_org[i])
                num_mater += 1
                j += 1
        elif dataset_org[i].find('rzewiark') != -1:
            if num_rzewiark < 28:
                test_validation_set.append(dataset_org[i])
                num_rzewiark += 1
                j += 1
        else:
            test_validation_set.append(dataset_org[i])
            j += 1
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
    tmp = train_set[i].strip('{"imageGcsUri":"gs://wozy_cropped/').split('","', 1)[0]
    tmp = tmp.split(".")[0]
    tmp = '/' + tmp
    tmp2 = tmp + '.'
    tmp = tmp + '_'
    # print(tmp)
    with open(f"{enriched_json_path}") as f:
        for line in f:
            if line.find(tmp) != -1 or line.find(tmp2) != -1:
                final_train_set.append(line)
print("final train set size: ", len(final_train_set))


tmp_length = len(train_set)
with open('jsw/split/v4_enriched_3003_training.jsonl', 'w') as f:
    j = 0
    num_urobkowy = 0
    num_obudowa = 0
    for i in range(len(final_train_set)):
        if final_train_set[i].find('urobkowy') != -1:
            if j < len(train_set):
                if num_urobkowy < 40:
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

with open('jsw/split/v4_tmp_enriched_3003_training.jsonl', 'w') as f:
    for i in range(len(final_train_set)):
        f.write(final_train_set[i])

with open('jsw/split/v4_tmp_enriched_3003_validaiton_test.jsonl', 'w') as f:
    for i in range(len(test_validation_set)):
        f.write(test_validation_set[i])

with open('jsw/split/v4_enriched_3003_validation.jsonl', 'w') as f:
    for i in range(len(validation_set)):
        f.write(validation_set[i])

with open('jsw/split/v4_enriched_3003_testing.jsonl', 'w') as f:
    for i in range(len(test_set)):
        f.write(test_set[i])
