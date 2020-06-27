import json
import logging

from flask import jsonify, request

from api import app
from model_factory import ModelFactory


def datatable_search():
    args = request.json if request.is_json else {}
    app.logger.debug("Input args: %s", args)

    data = ModelFactory.customer.datatable_search(args)

    customers = []
    for customer in data['customers']:
        cust_dict = customer.row2dict()
        cust_dict['address'] = customer.address.row2dict()
        cust_dict['address']['city'] = customer.address.city.row2dict()
        cust_dict['address']['city']['country'] = customer.address.city.country.row2dict()
        customers.append(cust_dict)

    response = {
        'fetch_id':  args.get('fetch_id'),
        'records_total': data['records_total'],
        'records_filtered': data['records_filtered'],
        'data': customers,
    }
    return response
