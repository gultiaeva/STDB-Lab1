from flask import Flask
from flask_orator import Orator

from database.credentials import user, password

app = Flask(__name__, template_folder='../templates')

app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'library',
        'user': user,
        'password': password,
        'use_qmark': True
    }
}

db = Orator(app)
