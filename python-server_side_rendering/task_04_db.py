from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def read_sqlite_db(db_path):
    data = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return data


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error_message = None

    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    elif source == 'sql':
        data = read_sqlite_db('products.db')
    else:
        error_message = "Wrong source"

    if product_id:
        product_id = int(product_id)
        data = [item for item in data if int(item['id']) == product_id]
        if not data:
            error_message = "Product not found"

    return render_template('product_display.html', products=data, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
