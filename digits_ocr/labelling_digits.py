from os import listdir
from os.path import isfile, join

jsons = []
for i in range(10):
    path = '/Desktop/work/jsw/digits/digit_numbers_classification/'+ str(i)
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print(str(i) + "  " + str(len(files)))
    for f in files:
        new_json = '{"imageGcsUri":"gs://wozy_digits/'+str(i)+'/'+f+'","boundingBoxAnnotations":[{"displayName":"'+str(i)+'","xMin":0.0,"xMax":1.0,"yMin":0.0,"yMax":1.0,"annotationResourceLabels":{"aiplatform.googleapis.com/annotation_set_name":"3245204171334352896"}}],"dataItemResourceLabels":{}}'
        jsons.append(new_json)
with open('/Desktop/work/jsw/digits/labelling.jsonl','w') as f:
    for line in jsons:
        f.write(line)
        f.write('\n')