import json
"""
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name', info['name'])
print('Hide', info['email']['hide'])
"""
inputs = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

infos = json.loads(inputs)
print("User count: ", len(infos))

for i in infos:
    print('Name: ', i['name'])
    print('ID: ', i["id"])
    print('Attribute: ', i['x'])