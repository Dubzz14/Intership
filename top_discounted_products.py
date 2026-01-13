from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="trial", 
        user="postgres",
        password="ezeh",
        cursor_factory=RealDictCursor 
    )

QUERY_1 = """
--Top discounted products

SELECT title, "discountPercentage"
FROM products_data
ORDER BY "discountPercentage" DESC
LIMIT 10; 
"""

@app.route('/category-analysis')
def get_analysis():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(QUERY_1)
        
        results = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)