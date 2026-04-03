from app import create_app, db
from app.models.user import User
from app.models.risk import Risk
from app.models.control import Control
from app.models.incident import Incident
from app.models.access import AccessLog, GovernanceAlert
# Phase 7, 8, 13 Imports
from app.models.vendor import Vendor
from app.models.dpdp import Consent
from app.models.dataflow import DataFlow

from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    print("Creating tables...")
    db.create_all()
    
    # 1. Admin & Dormant User
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', email='admin@grc.com', role='Admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

    dormant = User.query.filter_by(username='dormant_user').first()
    if not dormant:
        dormant = User(username='dormant_user', email='dormant@test.com', role='Risk Owner')
        dormant.set_password('password123')
        db.session.add(dormant)
        db.session.commit()

    # 2. Access Log
    if AccessLog.query.count() == 0:
        old_log = AccessLog(user_id=dormant.id)
        old_log.login_time = datetime.utcnow() - timedelta(days=40)
        db.session.add(old_log)

    # 3. Sample Risk
    if Risk.query.count() == 0:
        r1 = Risk(title="SQL Injection", impact=5, likelihood=4) # Critical
        r1.save()
        r2 = Risk(title="Weak Passwords", impact=3, likelihood=3) # Medium
        r2.save()

    # 4. Sample Control (For Compliance %)
    if Control.query.count() == 0:
        c1 = Control(name="Firewall Config", framework="ISO 27001", status="Implemented")
        db.session.add(c1)
        c2 = Control(name="Encryption Key Mgmt", framework="ISO 27001", status="Implemented")
        db.session.add(c2)
        c3 = Control(name="User Training", framework="ISO 27001", status="In Progress")
        db.session.add(c3)

    # 5. Sample Incident
    if Incident.query.count() == 0:
        inc = Incident(title="Malware Detection", severity="High", assigned_to=1)
        db.session.add(inc)

    # 6. Phase 7: Sample Vendor
    if Vendor.query.count() == 0:
        v1 = Vendor(name="Cloud Corp", service_type="Hosting", risk_score=85)
        db.session.add(v1)
        v2 = Vendor(name="SecurePay", service_type="Payments", risk_score=30)
        db.session.add(v2)

    # 7. Phase 8: Sample DPDP Consent
    if Consent.query.count() == 0:
        con1 = Consent(data_principal="user1@gmail.com", purpose="Marketing", status="Active")
        db.session.add(con1)
        con2 = Consent(data_principal="user2@gmail.com", purpose="Analytics", status="Revoked")
        db.session.add(con2)

    # 8. Phase 13: Sample Data Flow
    if DataFlow.query.count() == 0:
        f1 = DataFlow(source_system="Mobile App", destination="Analytics DB", data_type="PII")
        db.session.add(f1)
        f2 = DataFlow(source_system="Web Portal", destination="Vendor Server", data_type="Financial")
        db.session.add(f2)

    db.session.commit()
    print("✅ All Data Seeded Successfully!")