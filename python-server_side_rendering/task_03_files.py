from flask import Flask, render_template, request
import json
import csv

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
