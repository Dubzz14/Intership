import json
import psycopg2
import os


json_string = '[{"name": "Alice","age": 22},{"name": "Alan","age": 32}]'

pyth_data = json.loads(json_string)

connection = connection = psycopg2.connect(dbname = os.getenv("DB_NAME","Intern"), user = os.getenv("DB_USER","postgres"), password = os.getenv("DB_PASS","ezeh"), host = os.getenv("DB_HOST","localhost"))


cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS json_data (name TEXT, age INTEGER);")

for record in pyth_data:
    cur.execute("INSERT INTO json_data (name,age) VALUES(%s,%s)", (record['name'], record['age']))

connection.commit()
print("Data successfully moved")


cur.execute("SELECT * FROM json_data")
data_from_db = cur.fetchall()
print (data_from_db)


cur.close()
connection.close()