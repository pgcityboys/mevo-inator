class StationModel:
    def __init__(self, id: int, code: str, address: str, coordinates: dict[float, float], park_zone: list[dict]):
        self.id = id
        self.code = code
        self.address = address
        self.coordinates = coordinates
        self.park_zone = park_zone

    def serialize(self):
        return {
            "id": self.id,
            "code": self.code,
            "address": self.address,
            "coordinates": self.coordinates,
            "park_zone": self.park_zone
        }