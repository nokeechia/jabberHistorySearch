from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys
import os

app = Flask(__name__, static_folder='C:\\Users\\U6019995\\Documents\\MyJabberFiles\\keech.achara@thomsonreuters.com\\')
#C:/Program%20Files%20(x86)/Cisco%20Systems/Cisco%20Jabber/Emoticons/
app.debug = True
print(os.path.join('sqlite:///', sys.argv[1]))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sys.argv[1]
db = SQLAlchemy(app)


if __name__ == '__main__':
    from views import *
    app.run()

