from app import db
from datetime import datetime, timedelta

class AccessLog(db.Model):
    __tablename__ = 'access_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50), default='192.168.1.1') # Dummy IP

class GovernanceAlert(db.Model):
    __tablename__ = 'governance_alerts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    alert_type = db.Column(db.String(50), nullable=False) # e.g., 'Dormant Account', 'No MFA'
    severity = db.Column(db.String(20), default='Medium') # High, Low
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.alert_type,
            "severity": self.severity,
            "description": self.description,
            "created_at": self.created_at.strftime('%Y-%m-%d')
        }