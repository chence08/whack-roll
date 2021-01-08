import os, json

dirs = os.listdir(".")
dic = {}
count = 0

for i in sorted(dirs):
	if i != 'scrape.py' and i != 'test.json':
		dic.update({count : i})
		count += 1
	
with open('test.json', 'w') as json_file:
	json.dump(dic, json_file)