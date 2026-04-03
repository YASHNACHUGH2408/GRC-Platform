from flask import Blueprint, request, jsonify
from app.models.control import Control
from app import db

control_bp = Blueprint('control', __name__)

# 1. Add New Control
@control_bp.route('/controls', methods=['POST'])
def add_control():
    data = request.get_json()
    
    new_control = Control(
        name=data['name'],
        description=data.get('description', ''),
        framework=data['framework'], # e.g., 'DPDP', 'ISO'
        status=data.get('status', 'In Progress'),
        effectiveness_score=data.get('score', 0),
        risk_id=data.get('risk_id')
    )
    
    db.session.add(new_control)
    db.session.commit()
    
    return jsonify({"message": "Control added", "control": new_control.to_dict()}), 201

# 2. Get All Controls
@control_bp.route('/controls', methods=['GET'])
def get_controls():
    # Filter by framework if provided (e.g., ?framework=DPDP)
    framework_filter = request.args.get('framework')
    
    query = Control.query
    if framework_filter:
        query = query.filter_by(framework=framework_filter)
        
    controls = query.all()
    output = [c.to_dict() for c in controls]
    return jsonify(output), 200

# 3. Get Compliance Score (Dashboard ke liye important)
@control_bp.route('/compliance/stats', methods=['GET'])
def get_compliance_stats():
    # Framework list define karo
    frameworks = ['ISO 27001', 'DPDP Act', 'GDPR']
    stats = {}
    
    for fw in frameworks:
        total_controls = Control.query.filter_by(framework=fw).count()
        if total_controls == 0:
            stats[fw] = {"total": 0, "implemented": 0, "percentage": 0}
            continue
            
        implemented_controls = Control.query.filter_by(framework=fw, status='Implemented').count()
        percent = (implemented_controls / total_controls) * 100
        
        stats[fw] = {
            "total": total_controls,
            "implemented": implemented_controls,
            "percentage": round(percent, 2)
        }
        
    return jsonify(stats), 200

# 4. Update Control
@control_bp.route('/controls/<int:id>', methods=['PUT'])
def update_control(id):
    control = Control.query.get_or_404(id)
    data = request.get_json()
    
    control.status = data.get('status', control.status)
    control.effectiveness_score = data.get('score', control.effectiveness_score)
    
    db.session.commit()
    return jsonify({"message": "Control updated", "control": control.to_dict()}), 200