# Используем официальный образ Python с поддержкой Django
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями проекта в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое проекта в контейнер
COPY . /app/

# Открываем порт для приложения
EXPOSE 8000

# Выполняем миграции и запускаем сервер Django
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
