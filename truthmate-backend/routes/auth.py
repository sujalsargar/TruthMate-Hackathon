from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
import os
from models.user import User
from extensions import db

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

@auth_bp.route('/signup', methods=['POST'])
def signup():
    # Signup logic
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    # Login logic
    pass

@auth_bp.route('/google-signin', methods=['POST'])
def google_signin():
    # Google OAuth logic
    pass