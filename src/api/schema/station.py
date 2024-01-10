from flask_marshmallow import Schema

class StationSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["id", "code", "address", "coordinates", "park_zone"]
