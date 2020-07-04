from flask import jsonify

from models import Language


def get_languages():
    rows = Language.query.order_by(
        Language.name.asc()).all()
    languages = list(map(lambda row: row.row2dict(), rows))
    return jsonify(languages)
