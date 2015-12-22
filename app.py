from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keech.achara@thomsonreuters.com.db'
db = SQLAlchemy(app)


if __name__ == '__main__':
    from views import *
    app.run()

