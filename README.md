# mevo-inator
Microservice to get MEVO points

### Getting started
Install dependencies
```
pip install -r requirements.txt
```

Run app in debug mode
```
flask run --debug
```

Port can be set with env variable. E.g. `FLASK_RUN_PORT=2137`. To do this in development mode you can use `.flaskenv` file.
More options can be found in https://flask.palletsprojects.com/en/3.0.x/cli/.

### Documentation
- Flask: https://flask.palletsprojects.com/en/3.0.x/quickstart/
- Schemas: https://flask-marshmallow.readthedocs.io/en/latest/

### API
`GET /api/stations`
#### Params
- lat (optional) - Latitude of position to look for closest stations from.
- lon (optional) - Longitude of position to look for closes stations from.
Result
```
{
  "data": [
    {
      "id": str,
      "code": str,
      "address": str,
      "coordinates": {
        "lat": float,
        "lon": float
      }
      park_zone: [
        {
          "lat": float,
          "lon": float
        }
      ]
    }
  ]
}
```

`GET /api/vehicles/<id>`
```
{
  "parking_slots_available": int,
  "vehicles_available": [
    {
      "vehicle_type_id": str,
      "count": int
    }
  ]
}
```
