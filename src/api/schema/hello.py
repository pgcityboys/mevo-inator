from flask_marshmallow import Schema

class HelloSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["message"]