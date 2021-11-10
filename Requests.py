import requests
r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
print(r)
print(r.status_code)
print(r.text)
print(type(r.text))
import json
question = json.loads(r.text)
print(question)
print(type(question))
import pprint
pprint.pprint(question)
print(question['results'][0]['incorrect_answers'])
person = { 'Name': 'Chaima', 'Age': 20}
person_json = json.dumps(person)
print(person_json)
print(type(person_json))