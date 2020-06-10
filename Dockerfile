FROM tiangolo/meinheld-gunicorn-flask:python3.7

ENV PORT 5000

EXPOSE 5000

COPY . /app

RUN pip install -r /app/requirements.txt

ENV FLASK_ENV=production
