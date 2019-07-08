# services/users/project/api/models.py


from mongoengine.document import Document
from mongoengine.fields import StringField, BooleanField, DateTimeField
import datetime


class User(Document):
    def to_json(self):
        return {
            'username': self.username,
            'email': self.email,
            'active': self.active
        }

    username = StringField(required=True)
    email = StringField(required=True)
    active = BooleanField(default=True)
    created_date = DateTimeField(default=datetime.datetime.utcnow)
