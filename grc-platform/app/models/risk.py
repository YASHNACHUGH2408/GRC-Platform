from app import db
from datetime import datetime

class Risk(db.Model):
    __tablename__ = 'risks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Scoring Parameters (1 to 5 scale)
    impact = db.Column(db.Integer, nullable=False)       # 1 (Low) to 5 (Critical)
    likelihood = db.Column(db.Integer, nullable=False)  # 1 (Rare) to 5 (Certain)
    
    # Derived Fields
    risk_score = db.Column(db.Integer, nullable=False)  # Impact * Likelihood
    risk_level = db.Column(db.String(50), nullable=False) # Low, Medium, High, Critical
    
    # Management
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    status = db.Column(db.String(50), default='Open') # Open, Mitigated, Accepted
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def calculate_score(self):
        # Score Formula: Impact x Likelihood
        self.risk_score = self.impact * self.likelihood
        
        # Auto Decide Risk Level
        if self.risk_score <= 4:
            self.risk_level = "Low"
        elif self.risk_score <= 9:
            self.risk_level = "Medium"
        elif self.risk_score <= 16:
            self.risk_level = "High"
        else:
            self.risk_level = "Critical"

    def save(self):
        self.calculate_score()
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "impact": self.impact,
            "likelihood": self.likelihood,
            "score": self.risk_score,
            "level": self.risk_level,
            "status": self.status,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }