import random

dataset_enriched = []
dataset_org = []
# tmp_list = ['18_18', '29_06', '9_06']
tmp_list = ['/9_06']
abc = '9_06'
ddd = '/' + abc
print(ddd)
for i in range(len(tmp_list)):
    with open('jsw/enriched/enriched_1716.jsonl') as f:
        for line in f:
            if line.find(tmp_list[i]) != -1:
                print(line)
                dataset_enriched.append(line)
print("whole enriched dataset size: ", len(dataset_enriched))
for i in range(len(dataset_enriched)):
    dataset_enriched[i] = dataset_enriched[i].strip('{"imageGcsUri":"gs://wozy_jsw/').split('","', 1)[0]
    print(dataset_enriched[i])
