from app import db
from datetime import datetime

class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    service_type = db.Column(db.String(100)) # Cloud, Consulting, etc.
    risk_score = db.Column(db.Integer, default=50) # 0-100
    contract_expiry = db.Column(db.Date, nullable=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "service": self.service_type,
            "risk_score": self.risk_score,
            "expiry": str(self.contract_expiry)
        }