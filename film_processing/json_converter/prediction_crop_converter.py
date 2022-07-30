import json
import jsonlines

with open('/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/result_batch_object_detection_v1.jsonl', 'r') as json_file:
    json_list = list(json_file)
actual_value = 'object'

data = []
for json_str in json_list:
    result = json.loads(json_str)
    tmp = {}
    prediction = {}
    obj1 = {}
    obj2 = {}
    obj3 = {}
    boundingBoxAnnotations = []
    obj1['displayName'] = 'Object'
    obj1['xMin'] = result['prediction']['bboxes'][0][0]
    obj1['xMax'] = result['prediction']['bboxes'][0][1]
    obj1['yMin'] = result['prediction']['bboxes'][0][2]
    obj1['yMax'] = result['prediction']['bboxes'][0][3]
    obj1['annotationResourceLabels'] = ''
    obj1['confidence'] = result['prediction']['confidences'][0]
    obj2['displayName'] = 'Object'
    obj2['xMin'] = result['prediction']['bboxes'][1][0]
    obj2['xMax'] = result['prediction']['bboxes'][1][1]
    obj2['yMin'] = result['prediction']['bboxes'][1][2]
    obj2['yMax'] = result['prediction']['bboxes'][1][3]
    obj2['annotationResourceLabels'] = ''
    obj2['confidence'] = result['prediction']['confidences'][0]
    obj3['displayName'] = 'Object'
    obj3['xMin'] = result['prediction']['bboxes'][2][0]
    obj3['xMax'] = result['prediction']['bboxes'][2][1]
    obj3['yMin'] = result['prediction']['bboxes'][2][2]
    obj3['yMax'] = result['prediction']['bboxes'][2][3]
    obj3['annotationResourceLabels'] = ''
    obj3['confidence'] = result['prediction']['confidences'][0]
    boundingBoxAnnotations.append(obj1)
    boundingBoxAnnotations.append(obj2)
    boundingBoxAnnotations.append(obj3)
    tmp['imageGcsUri'] = result['instance']['content']
    tmp['boundingBoxAnnotations'] = boundingBoxAnnotations
    data.append(tmp)
    # print(f"result: {result['instance']}")
    # print(isinstance(result, dict))
with jsonlines.open('result_v1.jsonl', 'w') as writer:
    writer.write_all(data)

  # {"instance": {"content": "gs://wozy_wagon_object_detection/v1/129.png", "mimeType": "image/png"}, "prediction": {
  #     "ids": ["3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656",
  #             "3983537224502214656", "3983537224502214656", "3983537224502214656", "3983537224502214656"],
  #     "displayNames": ["object", "object", "object", "object", "object", "object", "object", "object", "object",
  #                      "object", "object", "object", "object", "object", "object", "object", "object", "object",
  #                      "object", "object", "object", "object", "object", "object", "object", "object", "object",
  #                      "object", "object", "object", "object", "object", "object", "object", "object", "object",
  #                      "object", "object", "object", "object"],
  #     "confidences": [0.9998523, 0.99391866, 0.7750716, 0.08861448, 0.05281629, 7.960101E-4, 7.8685046E-4, 4.2793035E-4,
  #                     3.085498E-4, 2.551115E-4, 2.4639422E-4, 1.9814227E-4, 1.3734627E-4, 1.11556656E-4, 7.898853E-5,
  #                     7.12408E-5, 4.0181385E-5, 3.7865913E-5, 3.4329E-5, 1.8381383E-5, 1.1285514E-5, 1.0221374E-5,
  #                     5.5057576E-6, 1.4381079E-6, 1.0378774E-6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
  #                     0.0, 0.0, 0.0, 0.0],
  #     "bboxes": [[0.564636, 0.99555564, 0.5004089, 0.99926484], [0.34602404, 0.6293245, 0.3776875, 0.7834026],
  #                [0.24719653, 0.4147068, 0.33834112, 0.5638394], [0.2154878, 0.32016304, 0.30824432, 0.458154],
  #                [0.22533299, 0.3440547, 0.3204642, 0.49323967], [0.78259426, 0.9636299, 0.4761862, 0.95486766],
  #                [0.91405976, 0.99479675, 0.7951608, 0.98611355], [0.9389268, 0.9912145, 0.7194046, 0.986168],
  #                [0.50359917, 0.93095636, 0.016438603, 0.26801994], [0.01069206, 0.094937176, 0.082582265, 1.0],
  #                [0.24463595, 0.5883405, 0.34306422, 0.70726544], [0.9050436, 0.9925152, 0.8704752, 0.9950706],
  #                [0.260664, 0.693708, 0.40938047, 0.8241419], [0.74967146, 0.974157, 0.03902666, 0.49876595],
  #                [0.18612453, 0.9089458, 0.73403645, 0.99373746], [0.02026011, 0.22296979, 0.05580592, 0.4551717],
  #                [0.009919189, 0.15359306, 0.11041411, 0.73295563], [0.0635404, 0.45110893, 0.019606313, 0.24183019],
  #                [0.03741406, 0.33455276, 0.033181854, 0.32172534], [0.09232271, 0.74974847, 0.028357174, 0.25212055],
  #                [0.04516734, 0.34437412, 0.6944378, 0.9717189], [0.024463415, 0.50553715, 0.7349532, 0.9740332],
  #                [0.045670837, 0.2301701, 0.56022745, 0.9781773], [0.1879748, 0.5704548, 0.24051972, 0.58726394],
  #                [0.57616174, 0.9057956, 0.45524755, 0.8545885], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0],
  #                [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0],
  #                [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0],
  #                [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0],
  #                [0.0, 0.0, 0.0, 0.0]]}}

  # {"imageGcsUri": "gs://wozy_jsw/36_03.png", "boundingBoxAnnotations": [
  #     {"displayName": "object", "xMin": 0.7703646237393328, "xMax": 0.9984484096198604, "yMin": 0.5462068965517242,
  #      "yMax": 0.9944827586206896,
  #      "annotationResourceLabels": {"aiplatform.googleapis.com/annotation_set_name": "3245204171334352896"}},
  #     {"displayName": "object", "xMin": 0.3886733902249806, "xMax": 0.8169123351435221, "yMin": 0.4289655172413793,
  #      "yMax": 0.8951724137931034,
  #      "annotationResourceLabels": {"aiplatform.googleapis.com/annotation_set_name": "3245204171334352896"}}],
  #  "dataItemResourceLabels": {}}
  #
  #
  # {
  #     "instance": {
  #         "content": "gs://wozy_cropped_3003_org_aug/7_10.png",
  #         "mimeType": "image/png"
  #     },
  #     "isTrue": "False",
  #     "actual": "JZR_215_01",
  #     "prediction": {
  #         "id": "1890981878891020288",
  #         "predicted": "urobkow",
  #         "confidences": 0.8927914,
  #         "bboxes": [
  #             0.0,
  #             1.0,
  #             0.0,
  #             1.0
  #         ]
  #     }
  # },