import os
from flask import Blueprint, jsonify, request, send_file

from ..models import get_session, InventoryItem

inventory_bp = Blueprint('inventory', __name__)


@inventory_bp.route('/inventory')
def list_inventory():
    session = get_session()
    try:
        items = session.query(InventoryItem).all()
        return jsonify([item.to_dict() for item in items])
    finally:
        session.close()


@inventory_bp.route('/inventory/<int:item_id>')
def get_inventory_item(item_id):
    session = get_session()
    try:
        item = session.query(InventoryItem).filter_by(id=item_id).first()
        if item:
            return jsonify(item.to_dict())
        return jsonify({'error': 'Item not found'}), 404
    finally:
        session.close()


@inventory_bp.route('/inventory', methods=['POST'])
def create_inventory_item():
    session = get_session()
    try:
        data = request.get_json()
        item = InventoryItem(
            sku=data['sku'],
            name=data['name'],
            description=data.get('description'),
            quantity=data.get('quantity', 0),
            unit_price=data.get('unit_price', 0.0),
            warehouse_location=data.get('warehouse_location')
        )
        session.add(item)
        session.commit()
        return jsonify(item.to_dict()), 201
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()


@inventory_bp.route('/export/<filename>')
def export_report(filename):
    # VULNERABLE: No path validation
    filepath = os.path.join('/app/reports', filename)
    return send_file(filepath)
