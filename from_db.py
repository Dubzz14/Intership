import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "ezeh"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route("/records", methods=["GET"])
def get_all_records():
    records = []
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM your_table_name;")
        db_records = cur.fetchall()

        column_names = [desc[0] for desc in cur.description]

        for record in db_records:
            records.append(dict(zip(column_names, record)))

    except (Exception, psycopg2.Error) as error:
        return jsonify({"error": str(error)}), 500
    finally:
        if conn:
            cur.close()
            conn.close()

    return jsonify(records)

if __name__ == "__main__":
    app.run(debug=True)