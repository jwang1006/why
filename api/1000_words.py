import csv, json
 
with open("api/1000 words.csv", 'r') as data:
  words = {}
  for line in csv.reader(data):
    val_list = [line[1], line[2]]
    engl_trans = ""
    for i in range(3, len(line)):
      engl_trans+=line[i]
    engl_trans = engl_trans.split(": Duration")[0]
    val_list.append(engl_trans)
    words[line[0]]=val_list
  print(words)

with open("api/1000_words.json", 'w') as f:
  json.dump(words, f)
