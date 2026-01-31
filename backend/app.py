from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="YOUR_DB_HOST",
    user="YOUR_DB_USER",
    password="YOUR_DB_PASSWORD",
    database="salesdb"
)

@app.route("/api/data")
def get_data():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sales")
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run()
