from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="frontend")

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/api/data")
def get_data():
    data = [
        {
            "product": "Pen",
            "quantity": 10,
            "total_sales": 100
        },
        {
            "product": "Book",
            "quantity": 5,
            "total_sales": 250
        }
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
