# app/routes.py
from flask import Blueprint, request, jsonify
from .utils.email_service import send_maintenance_request
from .utils.image_processor import process_image
import os

main = Blueprint('main', __name__)

@main.route('/api/maintenance-request', methods=['POST'])
def submit_maintenance_request():
    data = request.json
    required_fields = ['unit', 'description', 'priority', 'contact']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
        
    try:
        send_maintenance_request(data)
        return jsonify({'message': 'Maintenance request submitted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

