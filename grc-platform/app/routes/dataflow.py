from flask import Blueprint, jsonify
from app.models.dataflow import DataFlow
from app import db

flow_bp = Blueprint('flow', __name__)

@flow_bp.route('/dataflow/flows', methods=['GET'])
def get_flows():
    flows = DataFlow.query.all()
    return jsonify([f.to_dict() for f in flows]), 200