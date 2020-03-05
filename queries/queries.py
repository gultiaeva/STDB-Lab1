from models.orm_models import *


def get_all_books():
    books = Book.all()
    books_list = [book.to_dict() for book in books]
    return books_list


def get_book_by_isbn(isbn):
    books = Book.where('ISBN', '=', isbn).get()
    books_list = [book.to_dict() for book in books]
    return books_list


def get_books_by_author(first_name, last_name):
    # author = Author.where('FIRST_NAME', '=', first_name).where('LAST_NAME', '=', last_name).select('ID').get()
    books = db.select('''select b.* from library.book b 
                      join library.book_has_author bha on b.ID = bha.BOOK_ID
                      join library.author a on bha.AUTHOR_ID = a.ID 
                      where a.FIRST_NAME = ? and a.LAST_NAME = ?''', [first_name, last_name])

    books_list = [book for book in books]
    return books_list


def get_shelves_by_hall(hall_id):
    shelves = Hall.find(1).shelve().get()
    shelves_list = [shelve.to_dict() for shelve in shelves]
    return shelves_list


def get_all_authors():
    authors = Author.all()
    authors_list = [author.to_dict() for author in authors]
    return authors_list


def get_authors_by_country(short_nm='NULL', full_nm='NULL'):
    countries = Country.where('SHORT_NM', '=', short_nm).or_where('FULL_NM', '=', full_nm).select('ID').get()
    ids = [country.to_dict()['ID'] for country in countries]
    authors = Author.where_in('COUNTRY_ID', ids).get()
    authors_list = [author.to_dict() for author in authors]
    return authors_list
