from flask import Blueprint, request, jsonify
from app.models.access import AccessLog, GovernanceAlert
from app.models.user import User
from app import db
from datetime import datetime, timedelta

access_bp = Blueprint('access', __name__)

# 1. Log Access (Simulation)
@access_bp.route('/access/log', methods=['POST'])
def log_access():
    data = request.get_json()
    user_id = data.get('user_id')
    
    new_log = AccessLog(user_id=user_id)
    db.session.add(new_log)
    db.session.commit()
    
    return jsonify({"message": "Access logged"}), 201

# 2. Run Governance Scan (Auto-detect violations)
@access_bp.route('/governance/scan', methods=['POST'])
def run_governance_scan():
    # 1. Find Dormant Users (Not logged in for 30 days)
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    # Find users who have logged in, but last login was > 30 days ago
    # (Simplified logic: checking users whose latest log is old)
    subquery = db.session.query(
        AccessLog.user_id, 
        db.func.max(AccessLog.login_time).label('last_login')
    ).group_by(AccessLog.user_id).subquery()
    
    dormant_users = db.session.query(User).join(
        subquery, User.id == subquery.c.user_id
    ).filter(subquery.c.last_login < thirty_days_ago).all()
    
    alerts_created = 0
    
    for user in dormant_users:
        # Check if alert already exists
        existing = GovernanceAlert.query.filter_by(
            user_id=user.id, 
            alert_type='Dormant Account'
        ).first()
        
        if not existing:
            alert = GovernanceAlert(
                user_id=user.id,
                alert_type='Dormant Account',
                severity='Medium',
                description=f'User {user.username} has not logged in for 30+ days.'
            )
            db.session.add(alert)
            alerts_created += 1

    # 2. Detect Users without MFA (Simulation Logic)
    # Since we don't have MFA column in User yet, let's flag users named "test" or random
    # In real app, check if user.mfa_enabled == False
    no_mfa_users = User.query.filter(User.username != 'admin').all() # Mock logic
    
    for user in no_mfa_users:
         existing = GovernanceAlert.query.filter_by(
            user_id=user.id, 
            alert_type='No MFA'
        ).first()
         
         if not existing and alerts_created < 5: # Limiting alerts for demo
            alert = GovernanceAlert(
                user_id=user.id,
                alert_type='No MFA',
                severity='High',
                description=f'User {user.username} has Multi-Factor Authentication disabled.'
            )
            db.session.add(alert)
            alerts_created += 1
            
    db.session.commit()
    
    return jsonify({"message": f"Scan complete. {alerts_created} new alerts generated."}), 200

# 3. Get All Alerts
@access_bp.route('/governance/alerts', methods=['GET'])
def get_alerts():
    alerts = GovernanceAlert.query.order_by(GovernanceAlert.created_at.desc()).all()
    return jsonify([a.to_dict() for a in alerts]), 200