from flask import jsonify

from model_factory import ModelFactory


def get_categories():
    rows = ModelFactory.category.query.order_by(
        ModelFactory.category.name.asc()).all()
    categories = tuple(map(lambda row: row.row2dict(), rows))
    return jsonify(categories)
