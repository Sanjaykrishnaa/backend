from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from collections import OrderedDict
import json

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        
        if not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Invalid data format"}), 400
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets, default='', key=str.lower)
        
        response = OrderedDict([
            ("is_success", True),
            ("user_id", "john_doe_17091999"),
            ("email", "john@xyz.com"),
            ("roll_number", "ABCD123"),
            ("numbers", numbers),
            ("alphabets", alphabets),
            ("highest_lowercase_alphabet", [highest_lowercase_alphabet] if highest_lowercase_alphabet else [])
        ])
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
