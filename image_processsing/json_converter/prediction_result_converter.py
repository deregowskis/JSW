import json

with open('/Users/bilibala/Desktop/work/wozy_film/json_converter/result_v1.jsonl', 'r') as json_file:
    json_list = list(json_file)
# actual_value = 'object'

data = []
for json_str in json_list:
    result = json.loads(json_str)
    tmp = {}
    prediction = {}
    tmp['instance'] = result['instance']
    prediction['id'] = result['prediction']['ids'][0]
    prediction['predicted'] = result['prediction']['displayNames'][0]
    # if  result['prediction']['displayNames'][0] != actual_value:
    #     tag = 'False'
    # else:
    #     tag = 'True'
    prediction['confidences'] = result['prediction']['confidences'][0]
    prediction['bboxes'] = result['prediction']['bboxes'][0]
    # tmp['isTrue'] = tag
    # tmp['actual'] = actual_value
    tmp['prediction'] = prediction
    data.append(tmp)
    # print(f"result: {result['instance']}")
    # print(isinstance(result, dict))
with open('tmp.json', 'w') as f:
  json.dump(data, f, indent = 4, ensure_ascii=False)