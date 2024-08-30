from flask import Flask, jsonify, request
from flask_cors import CORS
from graph import get_shortest_path

app = Flask(__name__)
CORS(app)

@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.json
    start = data['start']
    end = data['end']
    path, distance = get_shortest_path(start, end)
    return jsonify({'path': path, 'distance': distance})

if __name__ == '__main__':
    app.run(debug=True)
