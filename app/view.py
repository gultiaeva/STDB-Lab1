from app import app
from flask import request
from flask import render_template
from queries import queries
from flask import jsonify


@app.route("/", methods=['GET'])
def test():
    return render_template('index.html')


@app.route("/books", methods=["GET"])
def get_books():
    list_of_books = []
    if request.args.get('isbn') is not None:
        list_of_books = queries.get_book_by_isbn(request.args.get('isbn'))
    elif all([request.args.get('first_name'), request.args.get('last_name')]):
        first_name, last_name = request.args.get('first_name'), request.args.get('last_name')
        list_of_books = queries.get_books_by_author(first_name, last_name)
    elif len(request.args) == 0:
        list_of_books = queries.get_all_books()
    return jsonify(list_of_books)


@app.route('/authors', methods=["GET"])
def get_authors():
    list_of_authors = []
    if any([request.args.get('short_nm'), request.args.get('full_nm')]):
        short_nm, full_nm = request.args.get('short_nm'), request.args.get('full_nm')
        list_of_authors = queries.get_authors_by_country(short_nm, full_nm)
    elif len(request.args) == 0:
        list_of_authors = queries.get_all_authors()
    return jsonify(list_of_authors)
