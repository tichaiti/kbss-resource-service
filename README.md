# kbss-resource-service

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

See [API-DOC](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/tichaiti/kbss-access-service/initial-impl/swagger_server/swagger/swagger.yaml) used for generation.

## To add additional apis:
Update [swagger.yaml](swagger_server/swagger/swagger.yaml)

Make sure your working directory is not this repo

Run `java -jar ./swagger-codegen-cli-3.0.18.jar generate -i kbss-resource-service/swagger_server/swagger/swagger.yaml -l python-flask -o kbss-resource-service`

Make sure you add your new controller(s) to [.swagger-codegen-ignore](.swagger-codegen-ignore)
 

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
