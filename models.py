from flask import jsonify
from xml.sax.saxutils import unescape
from app import db
import datetime
from time import mktime
from datetime import datetime
from sqlalchemy import types

class History_Message(db.Model):
    __tablename__ = 'history_message'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    payload = db.Column(db.CLOB)
    date = db.Column(db.Integer)
    sender = db.Column(db.Text)
    item = db.Column(db.Integer)
    label = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(History_Message, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<History_Messge: %s>' % self.id

    def as_dict(self):
        """ Return an individual history_Messages as a dictionary.
         """
        return {
            'id': self.id,
            'type': self.type,
            'payload': self.payload.replace("&lt;", "<"),
            'date': self.date,
            'sender': self.sender,
            'item': self.item,
            'label': self.label
        }


    @classmethod
    def jsonify_all(cls):
         """ Returns all Todo instances in a JSON
             Flask response.
         """
         return jsonify(history_Messages=[History_Message.as_dict() for History_Message in cls.query.all()])


class IntegerDateTime(types.TypeDecorator):
    """Used for working with epoch timestamps.

Converts datetimes into epoch on the way in.
    Converts epoch timestamps to datetimes on the way out.
    """
    impl = types.INTEGER

    def process_bind_param(self, value, dialect):
        return mktime(value.timetuple())

    def process_result_value(self, value, dialect):
        return datetime.fromtimestamp(value)
