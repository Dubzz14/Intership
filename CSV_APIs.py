import pandas as pd
import requests
from flask import Flask, jsonify

app = Flask(__name__)

df = pd.read_csv(r"C:\Users\HP\OneDrive\Downloads\transactions.csv")
print("Your data:")
dic = df.to_dict(orient = 'records')
print(dic)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify(dic)


if __name__ == '__main__':
    print("\nStarting API at http://localhost:5000/transactions")
    print("Open this URL in a browser to see the JSON data.")
    app.run(debug=True)

receipt = requests.get("http://localhost:5000/transactions")
print(receipt.json())