from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys
import os

app = Flask(__name__)
app.debug = True
print(os.path.join('sqlite:///', sys.argv[1]))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sys.argv[1]
db = SQLAlchemy(app)


if __name__ == '__main__':
    from views import *
    app.run()

