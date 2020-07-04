from flask import render_template

from controllers import category, country, customer, film, language

from . import app


@app.route("/api/countries")
def api_countries():
    return country.get_countries()


@app.route("/api/datatable/customers", methods=["POST"])
def api_datatable_customers():
    return customer.datatable_search()


@app.route("/api/categories")
def api_categories():
    return category.get_categories()


@app.route("/api/languages")
def api_languages():
    return language.get_languages()


@app.route("/api/datatable/films", methods=["POST"])
def api_datatable_films():
    return film.datatable_search()
