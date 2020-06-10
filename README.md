
## Requirementes

- Python 3
- Docker

## Python 3 (MacOSX)

```bash
brew install python
brew link --overwrite python
```

## Virtual Env

```bash
python3 -m venv venv
```

## Dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt
pip install <dependency>
pip freeze > requirements.txt
```


 ## Flyway

```bash
./bin/flyway.sh <ENV> <ACTION>
```

## Development

#### Database

```bash
docker run -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=py-rest-api -p 3306:3306 mysql:5.7
./bin/flyway.sh localhost migrate
```

#### Webserver

```bash
source venv/bin/activate
export FLASK_ENV=development && export FLASK_APP=main.py && flask run
```

## Docker
