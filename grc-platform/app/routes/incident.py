from flask import Blueprint, request, jsonify
from app.models.incident import Incident
from app import db

incident_bp = Blueprint('incident', __name__)

# 1. Report Incident
@incident_bp.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    
    new_incident = Incident(
        title=data['title'],
        description=data.get('description', ''),
        severity=data['severity'], # Low, Medium, High, Critical
        assigned_to=data.get('assigned_to')
    )
    
    db.session.add(new_incident)
    db.session.commit()
    
    return jsonify({"message": "Incident logged", "incident": new_incident.to_dict()}), 201

# 2. Get All Incidents
@incident_bp.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    output = [i.to_dict() for i in incidents]
    return jsonify(output), 200

# 3. Resolve Incident (Close ticket)
@incident_bp.route('/incidents/<int:id>/resolve', methods=['PUT'])
def resolve_incident(id):
    incident = Incident.query.get_or_404(id)
    incident.resolve()
    return jsonify({
        "message": "Incident resolved", 
        "mttr": f"{incident.calculate_mttr_hours()} hours"
    }), 200

# 4. Dashboard Stats (Total Open, Critical Count)
@incident_bp.route('/incidents/stats', methods=['GET'])
def incident_stats():
    total_open = Incident.query.filter_by(status='Open').count()
    critical_open = Incident.query.filter_by(severity='Critical', status='Open').count()
    resolved_count = Incident.query.filter_by(status='Resolved').count()
    
    return jsonify({
        "total_open": total_open,
        "critical_open": critical_open,
        "resolved": resolved_count
    }), 200