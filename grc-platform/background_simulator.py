import time
import random
import threading  # <--- YE MISSING THA
from app import create_app, db
from app.models.risk import Risk
from app.models.incident import Incident
from app.models.dpdp import Consent
from app.models.vendor import Vendor
from app.models.control import Control

def start_simulation():
    app = create_app()
    
    with app.app_context():
        print("🤖 SUPER CHAOS BOT STARTED: Simulating Live Enterprise Environment...")
        
        risk_titles = [
            "SQL Injection", "Phishing Attack", "Ransomware", 
            "Data Leak", "DDoS Attack", "Insider Threat"
        ]
        
        incident_titles = [
            "Server Down", "Login Failure Spike", "Malware Detected", 
            "Firewall Block", "Unauthorized Access"
        ]

        while True:
            try:
                # --- 1. RISK GENERATION ---
                if random.random() > 0.3: 
                    new_risk = Risk(
                        title=random.choice(risk_titles),
                        impact=random.randint(1, 5),
                        likelihood=random.randint(1, 5)
                    )
                    new_risk.save()
                    print(f"⚠️ [Risk] New: {new_risk.title} (Score: {new_risk.risk_score})")

                # --- 2. INCIDENT CHAOS ---
                if random.random() > 0.5:
                    new_inc = Incident(
                        title=random.choice(incident_titles),
                        severity=random.choice(["Low", "Medium", "High", "Critical"])
                    )
                    db.session.add(new_inc)
                    print(f"🚨 [Incident] Opened: {new_inc.title}")
                else:
                    open_inc = Incident.query.filter_by(status='Open').first()
                    if open_inc:
                        open_inc.resolve()
                        print(f"✅ [Incident] Resolved: {open_inc.title}")

                # --- 3. DPDP COMPLIANCE ---
                consents = Consent.query.all()
                if consents:
                    target_consent = random.choice(consents)
                    if target_consent.status == 'Active':
                        target_consent.status = 'Revoked'
                    else:
                        target_consent.status = 'Active'

                # --- 4. CONTROL DRIFT ---
                controls = Control.query.all()
                if controls:
                    target_ctrl = random.choice(controls)
                    if target_ctrl.status == 'Implemented':
                        target_ctrl.status = 'In Progress'
                    else:
                        target_ctrl.status = 'Implemented'

                # --- 5. VENDOR RISK ---
                vendors = Vendor.query.all()
                if vendors:
                    target_vendor = random.choice(vendors)
                    target_vendor.risk_score = random.randint(10, 99)

                db.session.commit()

            except Exception as e:
                print(f"❌ Bot Error: {e}")
                db.session.rollback()
            
            time.sleep(4)

# YE FUNCTION MISSING THA - YE LAST ME ADD HUA HAI
def start_bot_thread():
    thread = threading.Thread(target=start_simulation)
    thread.daemon = True
    thread.start()
    print("🚀 Background Bot Activated")