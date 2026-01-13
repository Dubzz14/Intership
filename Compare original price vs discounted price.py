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

QUERY_3 = """
--Compare original price vs discounted price

SELECT
    title,
    price AS original_price,
    (price - (price * ("discountPercentage" / 100.0))) AS discounted_price,
    "discountPercentage"
FROM
    public.products_data
ORDER BY
    price DESC
LIMIT 10;
"""

@app.route('/original vs discount')
def get_analysis():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(QUERY_3)
        
        results = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)