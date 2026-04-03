from flask import Blueprint, request, jsonify
from app.models.risk import Risk
from app import db

risk_bp = Blueprint('risk', __name__)

# 1. Create New Risk
@risk_bp.route('/risks', methods=['POST'])
def create_risk():
    data = request.get_json()
    
    new_risk = Risk(
        title=data['title'],
        description=data.get('description', ''),
        impact=int(data['impact']),
        likelihood=int(data['likelihood']),
        owner_id=data.get('owner_id'), # Optional
        status=data.get('status', 'Open')
    )
    
    # ye method score calculate karke save karega
    new_risk.save()
    
    return jsonify({"message": "Risk added", "risk": new_risk.to_dict()}), 201

# 2. Get All Risks
@risk_bp.route('/risks', methods=['GET'])
def get_risks():
    risks = Risk.query.all()
    # List me convert kar rahe hain
    output = [r.to_dict() for r in risks]
    return jsonify(output), 200

# 3. Get Single Risk (Optional)
@risk_bp.route('/risks/<int:id>', methods=['GET'])
def get_risk(id):
    risk = Risk.query.get_or_404(id)
    return jsonify(risk.to_dict()), 200

# 4. Update Risk (e.g., Mitigate it)
@risk_bp.route('/risks/<int:id>', methods=['PUT'])
def update_risk(id):
    risk = Risk.query.get_or_404(id)
    data = request.get_json()
    
    risk.status = data.get('status', risk.status)
    # Agar impact/likelihood update ki, to score recalculate hoga
    if 'impact' in data: risk.impact = int(data['impact'])
    if 'likelihood' in data: risk.likelihood = int(data['likelihood'])
    
    risk.save()
    
    return jsonify({"message": "Risk updated", "risk": risk.to_dict()}), 200

# 5. Delete Risk
@risk_bp.route('/risks/<int:id>', methods=['DELETE'])
def delete_risk(id):
    risk = Risk.query.get_or_404(id)
    db.session.delete(risk)
    db.session.commit()
    return jsonify({"message": "Risk deleted"}), 200