FROM python:3-alpine

WORKDIR /app
EXPOSE 80
# CMD ["gunicorn", "-w", "1", "--bind", "0.0.0.0:80", "app:app", "--timeout", "120"]
CMD ["python", "app.py"]
COPY Pipfile Pipfile.lock ./
RUN apk add --no-cache libpq postgresql-dev make g++ && \
  pip install pipenv && \
  pipenv install --system && \
  apk del postgresql-dev make g++

COPY app.py ./
