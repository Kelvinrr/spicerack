#!/usr/bin/env python3

import connexion

from spicerack import encoder
import os

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'spicerack'})
    app.run(port=8080)

    if "SPICE_DATA" not in os.environ:
        app.logger.error("$SPICE_DATA not set, exiting...")
        exit(1)

if __name__ == '__main__':
    main()
