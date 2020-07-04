from flask import jsonify

from models import Country


def get_countries():
    rows = Country.query.order_by(
        Country.country.asc()).all()
    countries = list(map(lambda row: row.row2dict(), rows))
    return jsonify(countries)
