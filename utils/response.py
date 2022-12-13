import json

from flask import jsonify

# from utils import JSONEncoder


def success_response(message, content=None, status_code=200):
    data = {'message': message, 'success': True}
    if content is not None:
        data['content'] = json.loads(json.dumps(content))
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp


def failure_response(message, status_code=400):
    data = {'message': message, 'success': False}
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp


def success_response_with_pagination(message, content=None, page_details=None, status_code=200):
    data = {'message': message, 'success': True}
    if content is not None:
        data['content'] = content
    if page_details is not None:
        data['pages_info'] = page_details
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp


def success_response_with_structure_pagination(message, structure=None, content=None, page_details=None,
                                               status_code=200):
    data = {'message': message, 'success': True}
    if content is not None:
        data['content'] = content
    if structure is not None:
        data['structure'] = structure
    if page_details:
        data['pages_info'] = page_details
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp


def failure_response_with_structure_pagination(message, structure=None, content=None, status_code=400):
    data = {'message': message, 'success': True}
    if content is not None:
        data['content'] = content
    if structure is not None:
        data['structure'] = structure
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp


def success_response_with_paf(message, content=None, page_details=None, additional_flag=None,
                                                     status_code=200):
    data = {'message': message, 'success': True, 'additional_flag': additional_flag}
    if content is not None:
        data['content'] = content
    if page_details is not None:
        data['pages_info'] = page_details

    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp


def success_response_with_af(message, content=None, additional_flag=None, status_code=200):
    data = {'message': message, 'success': True, "additional_flag": additional_flag}
    if content is not None:
        data['content'] = json.loads(json.dumps(content))
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp

