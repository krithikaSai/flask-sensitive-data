from flask import Flask, request, jsonify

app = Flask(__name__)

# Sensitive information (hardcoded for testing)
SENSITIVE_DATA = {
    "username": "admin",
    "password": "secretpassword",
    "api_key": "my-api-key-1234",
    "ip_address": "192.168.1.1"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == SENSITIVE_DATA['username'] and password == SENSITIVE_DATA['password']:
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)

