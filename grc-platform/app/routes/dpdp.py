from flask import Blueprint, jsonify
from app.models.dpdp import Consent
from app import db

dpdp_bp = Blueprint('dpdp', __name__)

@dpdp_bp.route('/dpdp/consents', methods=['GET'])
def get_consents():
    consents = Consent.query.all()
    return jsonify([c.to_dict() for c in consents]), 200