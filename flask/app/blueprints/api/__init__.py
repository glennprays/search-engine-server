from flask import Blueprint, request, render_template_string
from app.usecases.search import SearchUseCase

bp = Blueprint("api", __name__, url_prefix="/api")
search_ucs = SearchUseCase()

@bp.route("/")
def index():
    return "Search Kuy API"

@bp.route("/search")
def search_query():
    query_param = request.args.get('q', default='', type=str)
    return search_ucs.search_query(query_param)

@bp.route("/documents/<filename>")
def open_file(filename):
    file_path = f"./documents/{filename}"

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            text = file.read()

        formatted_text = f'<pre>{text}</pre>'
        return render_template_string(formatted_text)
    except FileNotFoundError:
        return "File not found", 404