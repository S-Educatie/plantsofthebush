FROM python:3-alpine

WORKDIR /app

RUN pip install Flask supabase python-dotenv flask_httpauth gunicorn

COPY . /app

ENV FLASK_ENV=production

CMD cd /app && gunicorn main:app
