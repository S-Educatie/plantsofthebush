FROM python:3-alpine

WORKDIR /app

COPY . /app

RUN pip install Flask supabase python-dotenv flask_httpauth

CMD cd /app && python main.py
