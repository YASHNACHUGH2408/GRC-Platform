from app import db
from datetime import datetime

class Incident(db.Model):
    __tablename__ = 'incidents'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Severity: Low, Medium, High, Critical
    severity = db.Column(db.String(50), nullable=False)
    
    # Status: Open, Investigating, Resolved
    status = db.Column(db.String(50), default='Open')
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)
    
    # Assigned User
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def resolve(self):
        self.status = 'Resolved'
        self.resolved_at = datetime.utcnow()
        db.session.commit()

    def calculate_mttr_hours(self):
        if self.status == 'Resolved' and self.resolved_at:
            delta = self.resolved_at - self.created_at
            return round(delta.total_seconds() / 3600, 2) # Convert to Hours
        return 0

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "severity": self.severity,
            "status": self.status,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M'),
            "mttr_hours": self.calculate_mttr_hours()
        }