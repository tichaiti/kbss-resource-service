#!/usr/bin/env python3

import connexion
from swagger_server import encoder
from swagger_server.config import configure_mongo, MONGO_DB


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'resource-service'}, pythonic_params=True)

    configure_mongo(app.app, MONGO_DB)

    app.run(port=8083)


if __name__ == '__main__':
    main()
