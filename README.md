
Simple REST API server written in Python using Flask and SQLAlchemy

## Pre-requisites

- Python 3
- Docker

### Create a Virtual Env

```bash
python3 -m venv venv
```

### Manage Dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt
pip install <dependency>
pip freeze > requirements.txt
```

### Development

#### Run local MYSQL Database

```bash
docker run -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=py-rest-api -p 3306:3306 mysql:5.7
```

#### Migrate Database with Flyway

```bash
./bin/flyway.sh localhost migrate
```

#### Run local Webserver

```bash
source venv/bin/activate
export FLASK_ENV=development && export FLASK_APP=main.py && flask run
```

### Docker

#### Build Image

```bash
docker build -t py-rest-api .
```

#### Run Image

```bash
docker run -p 5000:5000 \
           -e LOG_LEVEL=error \
           -e DB_HOST=docker.for.mac.host.internal \
           -e DB_PORT=3306 \
           -e DB_USER=root \
           -e DB_PASS=root \
           -e DB_NAME=py-rest-api \
        py-rest-api:latest
```

