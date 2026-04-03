from flask import Blueprint, jsonify
from app.models.vendor import Vendor
from app import db

vendor_bp = Blueprint('vendor', __name__)

@vendor_bp.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([v.to_dict() for v in vendors]), 200