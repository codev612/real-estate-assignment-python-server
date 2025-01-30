from flask import Blueprint, request, jsonify
from app.ml.model import train_model, analyze_listing

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    price = data['price']
    projected_revenue = data['projected_revenue']
    
    model = train_model()
    result = analyze_listing(model, price, projected_revenue)
    
    return jsonify({'high_potential': result})
