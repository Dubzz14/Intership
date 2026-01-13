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

QUERY_4 = """
--Identify underpriced or overpriced items

SELECT
    title,
    category,
    price,
    AVG(price) OVER (PARTITION BY category) AS category_avg_price,
    CASE
        WHEN price > AVG(price) OVER (PARTITION BY category) THEN 'Overpriced'
        WHEN price < AVG(price) OVER (PARTITION BY category) THEN 'Underpriced'
        ELSE 'Fairly Priced'
    END AS price_status
FROM
    products_data
ORDER BY
    price_status, category;
"""

@app.route('/under vs over')
def get_analysis():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(QUERY_4)
        
        results = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)