#!/usr/bin/env python3
import os

from swagger_server import encoder
from swagger_server.config import app, settings, db
from swagger_server.models.banner import Banner

app.app.json_encoder = encoder.JSONEncoder
specification = os.path.join(os.path.join(os.path.dirname(__file__), 'swagger'), 'swagger.yaml')
app.add_api(specification, arguments={'title': 'Maintenance'})

db.create_all()
if __name__ == '__main__':
    app.run(port=settings.APP_PORT)
