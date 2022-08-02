output_list = []
with open ('/Desktop/work/jsw/empty_full/three_classes_cropped_labels.jsonl') as f:
    for line in f:
        if line.count("UNDEFINED") == 0:
            output_list.append(line)

with open ('/Desktop/work/jsw/empty_full/two_classes_cropped_labels.jsonl', 'w') as f:
    for element in output_list:
        f.write(element)
