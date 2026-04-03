from app import db
from datetime import datetime

class Consent(db.Model):
    __tablename__ = 'consents'
    id = db.Column(db.Integer, primary_key=True)
    data_principal = db.Column(db.String(100), nullable=False) # User Email/ID
    purpose = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='Active') # Active, Revoked
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.data_principal,
            "purpose": self.purpose,
            "status": self.status
        }