import json
import psycopg2


json_string = '[{"name": "Alice","age": 22},{"name": "Alan","age": 32}]'

pyth_data = json.loads(json_string)

connection = psycopg2.connect(dbname = "Intern", user = "postgres", password = "ezeh", host ="localhost")

cur = connection.cursor()

cur.execute("CREATE TABLE json_data (name TEXT, age INTEGER);")

for record in pyth_data:
    cur.execute("INSERT INTO json_data (name,age) VALUES(%s,%s)", (record['name'], record['age']))

connection.commit()

cur.close()
connection.close()
print("Data successfully moved")
