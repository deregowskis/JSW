import random

# dataset_enriched = []
# dataset_org = []

# with open('jsw/enriched/enriched_1716.jsonl') as f:
#     for line in f:
#         if line.find("13_9") != -1:
#             print(line)
#             dataset_enriched.append(line)
# print("whole enriched dataset size: ", len(dataset_enriched))
# for i in range(len(dataset_enriched)):
#     dataset_enriched[i] = dataset_enriched[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","', 1)[0]
#     print(dataset_enriched[i])

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
#
cut = 0.2 * len(dataset_org)
validation_test_set = random.sample(dataset_org, round(cut))
print("validation_test size: ", len(validation_test_set))

train_set = [value for value in dataset_org if value not in validation_test_set]
print("train size: ", len(train_set))

cut = 0.5 * len(validation_test_set)
test_set = random.sample(validation_test_set, round(cut))
print("test size: ", len(test_set))

validation_set = [value for value in validation_test_set if value not in test_set]
print("validation size: ", len(validation_set))
#
final_train_set = []

for i in range(len(train_set)):
    tmp = train_set[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","', 1)[0]
    tmp = tmp.split(".")[0]
    tmp = '/' + tmp
    # print(tmp)
    with open('jsw/enriched/enriched_1716.jsonl') as f:
        for line in f:
            if line.find(tmp) != -1:
                final_train_set.append(line)
print("final train set size: ", len(final_train_set))
# #
final_test_set = []
tmp_list = []
for i in range(len(test_set)):
    tmp = test_set[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","', 1)[0]
    tmp = tmp.split(".")[0]
    tmp = '/' + tmp
    # print(tmp)
    with open('jsw/enriched/enriched_1716.jsonl') as f:
        for line in f:
            if line.find(tmp) != -1:
                # print(line)
                final_test_set.append(line)
print("final test set size: ", len(final_test_set))
# #
final_validation_set = []
for i in range(len(validation_set)):
    tmp = validation_set[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","', 1)[0]
    tmp = tmp.split(".")[0]
    tmp = '/' + tmp
    # print(tmp)
    with open('jsw/enriched/enriched_1716.jsonl') as f:
        for line in f:
            if line.find(tmp) != -1:
                # print(line)
                final_validation_set.append(line)
print("final validation set size: ", len(final_validation_set))

with open('jsw/split/enriched_1716_training.jsonl', 'w') as f:
    for i in range(len(final_train_set)):
        f.write(final_train_set[i])
#
with open('jsw/split/enriched_1716_validation.jsonl', 'w') as f:
    for i in range(len(final_validation_set)):
        f.write(final_validation_set[i])

with open('jsw/split/enriched_1716_testing.jsonl', 'w') as f:
    for i in range(len(final_test_set)):
        f.write(final_test_set[i])
########
with open('jsw/split/tmp_enriched_1716_training.jsonl', 'w') as f:
    for i in range(len(train_set)):
        f.write(train_set[i])

with open('jsw/split/tmp_enriched_1716_validation.jsonl', 'w') as f:
    for i in range(len(validation_set)):
        f.write(validation_set[i])

with open('jsw/split/tmp_enriched_1716_testing.jsonl', 'w') as f:
    for i in range(len(test_set)):
        f.write(test_set[i])
