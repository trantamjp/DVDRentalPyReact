from flask import jsonify

from models import Category


def get_categories():
    rows = Category.query.order_by(
        Category.name.asc()).all()
    categories = tuple(map(lambda row: row.row2dict(), rows))
    return jsonify(categories)
