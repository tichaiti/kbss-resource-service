#!/usr/bin/env python3
import os

import connexion
from swagger_server import encoder
from swagger_server.config import configure_mongo, MONGO_DB


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'resource-service'}, pythonic_params=True)

    configure_mongo(app.app, MONGO_DB)

    port = int(os.environ.get("PORT", default=8080))
    app.run(port=port)


if __name__ == '__main__':
    main()
