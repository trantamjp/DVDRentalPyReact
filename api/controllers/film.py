import json

from flask import jsonify, request

from api import app
from models import Film


def datatable_search():
    args = request.json if request.is_json else {}
    app.logger.debug("Input args: %s", args)

    data = Film.datatable_search(args)

    films = []
    for film in data['films']:
        film_dict = film.row2dict()
        film_dict['language'] = film.language.row2dict()
        film_dict['categories'] = [category.row2dict()
                                   for category in film.categories]
        film_dict['actors'] = [actor.row2dict() for actor in film.actors]
        films.append(film_dict)

    response = {
        'fetch_id':  args.get('fetch_id'),
        'records_total': data['records_total'],
        'records_filtered': data['records_filtered'],
        'data': films,
    }
    return response
