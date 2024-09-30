# Использование Python 3.10 в качестве базового образа
FROM python:3.10-slim

# Далее ваши команды для установки зависимостей и настройки проекта
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "rentapp.wsgi:application"]
