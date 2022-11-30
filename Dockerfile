FROM python:3.10-slim

WORKDIR /app/

COPY . .

RUN apt update && apt install gcc

RUN pip install -r requirements.txt

CMD ["gunicorn", "estudiantes.wsgi:application"]