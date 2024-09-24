from flask import Blueprint, jsonify, request
from .models import UserInfo
from .db import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = UserInfo.query.all()
    user_li = []
    for user in users:
        user_li.append(UserInfo.to_dict(user))

    # user_list = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    return jsonify(user_li)

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserInfo.query.get_or_404(user_id)
    return jsonify(UserInfo.to_dict(user))

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = UserInfo(name=data['name'], email=data['email'],password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = UserInfo.query.get_or_404(user_id)
    data = request.json
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserInfo.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

def success_response(data=None, message="Success"):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), 200

def error_response(message="Error", status_code=400):
    return jsonify({
        "status": "error",
        "message": message
    }), status_code