from flask import jsonify
from flask.views import MethodView

from models import Country


class CountryAPI(MethodView):
    def get(self):
        rows = Country.query.order_by(
            Country.country.asc()).all()
        countries = list(map(lambda row: row.row2dict(), rows))
        return jsonify(countries)
