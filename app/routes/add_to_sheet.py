from flask import Blueprint, request, jsonify
from app.google_sheets.sheet import append_to_sheet

add_to_sheet_bp = Blueprint('add_to_sheet', __name__)

@add_to_sheet_bp.route('/add_to_sheet', methods=['POST'])
def add_to_sheet():
    data = request.json
    price = data['price']
    link = data['link']
    
    append_to_sheet(price, link)
    
    return jsonify({'status': 'success'})
