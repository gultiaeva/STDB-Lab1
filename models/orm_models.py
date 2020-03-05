from orator.orm import belongs_to
from orator.orm import has_many
from orator.orm import has_many_through
from app import db


class ShelveHasBook(db.Model):
    __table__ = 'SHELVE_has_BOOK'
    __fillable__ = ['INSTANCES_LEFT']
    __timestamps__ = False

    @belongs_to('ID', 'BOOK_ID')
    def book(self):
        return Book

    @belongs_to('ID', 'HALL_ID')
    def hall(self):
        return Hall


class BookHasAuthor(db.Model):
    __table__ = 'BOOK_has_AUTHOR'
    __fillable__ = []
    __timestamps__ = False

    @belongs_to('ID', 'BOOK_ID')
    def book(self):
        return Book

    @belongs_to('ID', 'AUTHOR_ID')
    def author(self):
        return Author


class Book(db.Model):
    __table__ = 'BOOK'
    __fillable__ = ['NAME', 'PART', 'ISBN', 'YEAR']
    __timestamps__ = False

    @has_many('SHELVE_ID', 'ID')
    def book_has_shelve(self):
        return Shelve

    @has_many('BOOK_ID', 'ID')
    def book_has_author(self):
        return Author


class Author(db.Model):
    __table__ = 'AUTHOR'
    __fillable__ = ['FIRST_NAME', 'LAST_NAME', 'PATRONYMIC', 'BIRTH_DATE']
    __timestamps__ = False

    @has_many('AUTHOR_ID', 'ID')
    def author_has_book(self):
        return BookHasAuthor

    @belongs_to('COUNTRY_ID', 'ID')
    def country(self):
        return Country


class Country(db.Model):
    __table__ = 'COUNTRY'
    __fillable__ = ['SHORT_NM', 'FULL_NM']
    __timestamps__ = False

    @has_many('COUNTRY_ID', 'ID')
    def author(self):
        return Author


class Shelve(db.Model):
    __table__ = 'SHELVE'
    __fillable__ = ['SHELVE_IDX']
    __timestamps__ = False

    @has_many_through(ShelveHasBook, 'SHELVE_ID', 'BOOK_ID')
    def book(self):
        return Book

    @belongs_to('SHELVE_ID', 'ID')
    def hall(self):
        return Hall


class Hall(db.Model):
    __table__ = 'HALL'
    __fillable__ = ['SHORT_NM', 'FULL_NM']
    __timestamps__ = False

    @has_many('HALL_ID', 'ID')
    def shelve(self):
        return Shelve
