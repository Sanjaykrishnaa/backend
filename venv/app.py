from flask import Flask, request, jsonify, make_response
from collections import OrderedDict
import json

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        
        # Separate numbers and alphabets while preserving the order
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Find the highest lowercase alphabet
        lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets, default='', key=str.lower)
        
        # Construct response using OrderedDict to maintain key order
        response = OrderedDict([
            ("is_success", True),
            ("user_id", "john_doe_17091999"),  # Replace with actual user ID logic
            ("email", "john@xyz.com"),  # Replace with actual email
            ("roll_number", "ABCD123"),  # Replace with actual roll number
            ("numbers", numbers),
            ("alphabets", alphabets),
            ("highest_lowercase_alphabet", [highest_lowercase_alphabet] if highest_lowercase_alphabet else [])
        ])
        
        # Convert OrderedDict to JSON string to preserve key order
        response_json = json.dumps(response)
        
        # Return response with appropriate headers
        return make_response(response_json, 200, {'Content-Type': 'application/json'})
    
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
