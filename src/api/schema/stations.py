from flask_marshmallow import Schema

class StationsSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["data"]
