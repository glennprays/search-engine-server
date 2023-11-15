from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/")
def index():
    return "Search Kuy API"

@bp.route("/search")
def search_query():
    query_param = request.args.get('q', default='', type=str)
    return jsonify({"query": query_param})