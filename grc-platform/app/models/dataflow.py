from app import db

class DataFlow(db.Model):
    __tablename__ = 'data_flows'
    id = db.Column(db.Integer, primary_key=True)
    source_system = db.Column(db.String(100)) # e.g., "Mobile App"
    destination = db.Column(db.String(100))   # e.g., "CRM Database"
    data_type = db.Column(db.String(50))      # e.g., "PII", "Financial"

    def to_dict(self):
        return {
            "id": self.id,
            "source": self.source_system,
            "dest": self.destination,
            "type": self.data_type
        }