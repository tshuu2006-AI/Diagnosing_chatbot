from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
from flask_cors import CORS
CORS(app)

# Rasa server URL
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/chat', methods=['POST'])
def chat():
    # Get user input from the request
    user_input = request.json.get('message')
    sender_id = request.json.get('sender', 'default')  # Default sender ID if not provided

    # Send user input to Rasa server
    payload = {
        "sender": sender_id,
        "message": user_input
    }
    response = requests.post(RASA_URL, json=payload)

    # Return the Rasa response to the client
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to connect to Rasa server"}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)