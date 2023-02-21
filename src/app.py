from flask import Flask, request, jsonify


products =[
    {'id': 1,'name':'product 1'},
    {'id': 2,'name':'product 2'},
    {'id': 3,'name':'product 3'},
    {'id': 4,'name':'product 4'},
    {'id': 5,'name':'product 5'},
    {'id': 6,'name':'product 6'},
]

app = Flask(__name__)


# calling the root route gives some info
@app.route('/')
def get_home():
    return "<h2>Please specify a path to get some records return</h2>"

# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    return jsonify(products), 200





if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=5500)