from app import db
from datetime import datetime

class Control(db.Model):
    __tablename__ = 'controls'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Framework: ISO 27001, DPDP Act, GDPR, etc.
    framework = db.Column(db.String(50), nullable=False) 
    
    # Status: Implemented, In Progress, Not Applicable
    status = db.Column(db.String(50), default='In Progress') 
    
    # Effectiveness Score (0-100%)
    effectiveness_score = db.Column(db.Integer, default=0)
    
    # Linked Risk ID (Optional: Risk ko mitigate karne ke liye)
    risk_id = db.Column(db.Integer, db.ForeignKey('risks.id'), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "framework": self.framework,
            "status": self.status,
            "score": self.effectiveness_score,
            "risk_id": self.risk_id
        }