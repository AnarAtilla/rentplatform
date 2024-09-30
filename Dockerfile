FROM python:3.10-slim

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libmysqlclient-dev \
    pkg-config \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Открываем порт
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
