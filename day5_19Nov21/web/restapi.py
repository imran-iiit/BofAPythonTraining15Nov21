# REST means Representational State Transfer; web services; 
#   GET, POST, PUT, DELETE methods to perform 
#   CRUD operations on db, which can be invoked on HTTP protocol
# REST Web APIs return JSON/XML (not HTML like in Web Services)

from flask import Flask, jsonify

app = Flask(__name__)

data = [
        {'id': 1, 'Name': 'Imran', 'job': 'AVP'}, 
        {'id': 2, 'Name': 'Imran2', 'job': 'AVP2'}, 
        {'id': 3, 'Name': 'Imran3', 'job': 'AVP3'}, 
       ]

@app.route('/', methods=['GET'])
def getDetails():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

# Run locally and check the web page result - http://127.0.0.1:5000/