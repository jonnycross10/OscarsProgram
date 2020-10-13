import json
d = {}
with open("data.json") as f:
  d = json.load(f)

search = "Good Will Hunting"
results = []

for i in range(0,11058):
  if(d[i]['entity']== search):
    results.append(d[i])

#prints out search results
print(str(results) + '\n')

#prints out search results filtered by category
s =sorted(results, key = lambda t: t['category'])
print(s)
