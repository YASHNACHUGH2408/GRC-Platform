from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # --- CONFIGURATION ---
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 
        'postgresql://grc_user:grc_pass@db:5432/grc_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

    # --- EXTENSIONS ---
    db.init_app(app)
    CORS(app)
    jwt.init_app(app)

    # --- REGISTER BLUEPRINTS (APIs) ---
    from app.routes.auth import auth_bp
    from app.routes.risk import risk_bp
    from app.routes.control import control_bp
    from app.routes.incident import incident_bp
    from app.routes.access import access_bp
    from app.routes.vendor import vendor_bp
    from app.routes.dpdp import dpdp_bp
    from app.routes.dataflow import flow_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(risk_bp, url_prefix='/api')
    app.register_blueprint(control_bp, url_prefix='/api')
    app.register_blueprint(incident_bp, url_prefix='/api')
    app.register_blueprint(access_bp, url_prefix='/api')
    app.register_blueprint(vendor_bp, url_prefix='/api')
    app.register_blueprint(dpdp_bp, url_prefix='/api')
    app.register_blueprint(flow_bp, url_prefix='/api')

    # --- PAGE ROUTES (FRONTEND) ---
    
    # 1. Landing Page Route (Root)
    @app.route('/')
    def landing():
        return render_template('landing.html')

    # 2. Dashboard Route
    @app.route('/dashboard')
    def dashboard():
        return render_template('index.html')

    return app