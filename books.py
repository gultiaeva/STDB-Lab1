from datetime import datetime
from credentials import user, password
import pymysql
from flask import jsonify


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


con = pymysql.connect(host='localhost',
                      user=user,
                      password=password,
                      database="library")


def read_all():
    """
    This function responds to a request for /api/books
    with the entire lists of books
    :return:        json string of list of books
    """

    with con:
        cur = con.cursor()
        cur.execute("""
        select book.NAME, 
               book.YEAR, 
               book.ISBN, 
               book.PART, 
               sum(shb.INSTANCES_LEFT) as INSTANCES_LEFT
            from book inner join shelve_has_book shb on book.ID = shb.BOOK_ID
            group by book.ID
            order by book.NAME;
            """)
        row_headers = [x[0] for x in cur.description]
        rows = cur.fetchall()
        json_data = []
        for result in rows:
            json_data.append(dict(zip(row_headers, result)))
        return jsonify(json_data)
