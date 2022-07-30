
urobkowy = []

with open('jsw/export/export.jsonl') as f:
    for line in f:
        if line.count("urobkowy") == 1:
            urobkowy.append(line)
print("Loaded {} 'urobkowy' photos to resample.".format(len(urobkowy)))

with open('jsw/export/urobkowy_sep.jsonl','w') as f:
    print("Start open urobkowy_sep")
    # with open('jsw/export/export.jsonl') as f2:
        # f.write(f2.read())
    for i in range(len(urobkowy)):
        f.write(urobkowy[i])
    print("Finished - urobkowy_sep")

