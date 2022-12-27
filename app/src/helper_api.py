from flask import Flask, request, jsonify, Blueprint
from src.shared.duo import sign
from src.shared.sharepoint import parse_results
from src.shared.texthelper import score_documents

# appFlask = Flask(__name__)

helper_api = Blueprint('helper_api', __name__)

@helper_api.route("/encryptduo", methods=['POST'])
def encrypt_duo_request():
    try:
        content_type = request.headers.get('Content-Type')
        request_body = None

        if (content_type == 'application/json'):
            request_body = request.json
        else:
            # handle failure
            pass

        method = request_body.get('Method')
        host = request_body.get("Host")
        path = request_body.get("Path")
        params = request_body.get("Params")

        duo_secret_key = request.headers.get('DuoSecretKey')
        duo_integration_key = request.headers.get('DuoIntegrationKey')

        try:
            response_body = sign(method, host, path, params, duo_secret_key, duo_integration_key)
            return jsonify(response_body)
        except Exception as exception:
            # handle more specific exception
            return jsonify(exception)
    except Exception as exception:
        return jsonify(exception)


@helper_api.route("/scoredocuments", methods=['POST'])
def score_results():
    try:
        content_type = request.headers.get('Content-Type')
        request_body = None

        if (content_type == 'application/json'):
            request_body = request.json
        else:
            # handle failure
            pass

        user_query = request_body.get('UserQuery')
        search_results = request_body.get('SearchResults')

        try:
            scored_documents = score_documents(user_query, search_results)
            return jsonify({
                "result": scored_documents
            })
        except Exception as exception:
            # handle more specific exception
            return jsonify(exception)


    except Exception as exception:
        return jsonify(exception)


@helper_api.route("/parsesharepointresults", methods=['POST'])
def parse_sharepoint_results():
    try:
        content_type = request.headers.get('Content-Type')
        request_body = None

        if (content_type == 'application/json'):
            request_body = request.json
            sharepoint_search_results = score_documents(request_body['query'], request_body['body'])
        else:
            # handle failure
            sharepoint_search_results = []
        # sharepoint_search_results = request_body.get('SharePointSearchResults')
        try:
            # return jsonify(parse_results(sharepoint_search_results))
            return jsonify(sharepoint_search_results)
        except Exception as exception:
            # handle more specific exception
            return jsonify(exception)

    except Exception as exception:
        return jsonify(exception)