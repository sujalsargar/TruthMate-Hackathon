from flask import Blueprint, request, jsonify
from models.verification import Verification
from models.user import User
from extensions import db
import jwt
import os
history_bp = Blueprint('history', __name__)

@history_bp.route('/all', methods=['GET'])
def get_history():
    # Get all user history
    pass

@history_bp.route('/<verification_id>', methods=['GET'])
def get_verification(verification_id):
    # Get single verification
    pass

@history_bp.route('/<verification_id>', methods=['DELETE'])
def delete_verification(verification_id):
    # Delete verification
    pass

@history_bp.route('/clear', methods=['DELETE'])
def clear_history():
    # Clear all history
    pass