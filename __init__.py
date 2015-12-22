from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keech.achara@thomsonreuters.com.db'
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    #print(History_Message.query.get(1))
    return 'Hello World!'

