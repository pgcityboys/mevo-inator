from flask_marshmallow import Schema

class VehiclesInfoSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["vehicles_avaiable", "parking_slots_available"]