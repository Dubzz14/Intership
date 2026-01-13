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

QUERY_9 = """
--Average discount percentage per category

SELECT
    category,
    AVG("discountPercentage") AS average_discount_pct
FROM
    products_data
GROUP BY
    category
ORDER BY
    average_discount_pct DESC;
"""

@app.route('/avg discount percent')
def get_analysis():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(QUERY_9)
        
        results = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)