from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

app = Flask(__name__)

# 🔐 JWT config
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Change this in production!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

# 🧪 Unprotected login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username == "admin" and password == "password":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify(msg="Bad username or password"), 401

# 🔐 Protected route
@app.route('/notes', methods=['GET'])
@jwt_required()
def get_notes():
    current_user = get_jwt_identity()
    return jsonify(notes=[{"note": "This is secure"}], user=current_user)

# ✅ Optional: Health check or home
@app.route('/', methods=['GET'])
def home():
    return "Secure Notes API is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

