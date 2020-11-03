import json
with open("data/coco/annotations/person_keypoints_train2017.json", "r") as f:
  dataset = json.load(f)
dataset['categories'] = [dataset['categories']]
with open("data/coco/annotations/person_keypoints_train2017.json", "w") as f:
  json.dump(dataset, f)
with open("data/coco/annotations/person_keypoints_val2017.json", "r") as f:
  dataset = json.load(f)
dataset['categories'] = [dataset['categories']]
with open("data/coco/annotations/person_keypoints_val2017.json", "w") as f:
  json.dump(dataset, f)
