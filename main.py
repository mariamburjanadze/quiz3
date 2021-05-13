import json
import sqlite3

import requests
conn = sqlite3.connect("factss.sqlite")
cursor = conn.cursor()
#ვქმნით ცხრილს იმ შემთხვევაში თუ იგი არ არის შექმნილი
try:
    cursor.execute('''create table factss(
    fact varchar(1000))''')
except:
    pass

number = input("number")
url = f'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number={number}'
res = requests.get(url)
txt = res.text
json_file = json.loads(txt)
betterversion = json.dumps(json_file, indent=4)

file = open("file.json", 'w')
file.write(betterversion)
file.close()

facts_list = [i['fact'] for i in json_file]
list_2 = []
database_list = cursor.execute("select * from factss")
for i in database_list:
    list_2.append(i[0])
for i in facts_list:
    if i not in list_2:
        cursor.execute("insert into factss (fact) values(?)", (i,))
conn.commit()
conn.close()
print(res.status_code)
