## RentApp: Система аренды недвижимости

## Описание проекта

**RentApp** — это платформа для аренды недвижимости, которая позволяет пользователям создавать объявления для аренды, бронировать жильё, управлять бронированиями и следить за аналитикой просмотров. Платформа поддерживает как арендаторов, так и арендодателей, предоставляя функциональные возможности для обоих типов пользователей.

### Функциональные возможности

- **Регистрация и авторизация**: Пользователи могут регистрироваться и входить в систему. Поддержка регистрации через email и авторизация через социальные сети (если настроено).
- **Управление профилем**: Возможность редактирования профиля и изменения пароля.
- **Управление объявлениями**: Пользователи могут создавать, редактировать и удалять свои объявления об аренде недвижимости.
- **Поиск объектов недвижимости**: Возможность поиска объектов недвижимости с фильтрами по ключевым словам.
- **Бронирование**: Арендаторы могут бронировать объекты, просматривать свои бронирования и отменять их при необходимости.
- **Аналитика**: Возможность отслеживания просмотров объявлений и истории поисковых запросов.
- **Уведомления**: Пользователи получают уведомления о бронированиях и других важных событиях.
- **Swagger и Redoc документация**: API документация доступна через Swagger и Redoc.

---

## Стек технологий

Проект построен с использованием следующих технологий:

- **Backend**: Django 4.x, Django Rest Framework (DRF)
- **Frontend**: Шаблоны Django (HTML, CSS)
- **Аутентификация**: Django Allauth
- **Документация API**: Swagger, Redoc
- **База данных**: SQLite (по умолчанию) или MySQL/PostgreSQL для продакшена
- **Контейнеризация**: Docker (планируется)
- **Хостинг и развертывание**: AWS (планируется)
- **Управление конфигурацией**: Python-dotenv

---

## Установка и запуск

### Шаги для локальной установки:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/rentapp.git
   cd rentapp
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   venv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` в корне проекта и добавьте следующие переменные окружения:
   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_HOST=smtp.yourmailserver.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   ```

5. Выполните миграции базы данных:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Создайте суперпользователя для доступа в админ-панель:
   ```bash
   python manage.py createsuperuser
   ```

7. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

8. Откройте браузер и перейдите на `http://127.0.0.1:8000/`.

---

## Структура проекта

- **`rentapp/`**: Основная папка проекта Django, содержащая настройки, маршруты и другие файлы конфигурации.
- **`user_service/`**: Модуль, отвечающий за управление пользователями (регистрация, авторизация, профили).
- **`property_service/`**: Модуль для управления объектами недвижимости.
- **`booking_service/`**: Модуль для бронирования объектов недвижимости.
- **`search_service/`**: Модуль для поиска и отображения истории поиска.
- **`analytics_service/`**: Модуль для аналитики просмотров и поисковых запросов.
- **`notification_service/`**: Модуль для отправки уведомлений.
- **`review_service/`**: Модуль для управления отзывами пользователей.
- **`templates/`**: HTML-шаблоны для рендеринга страниц.
- **`static/`**: Статические файлы, такие как CSS, JS и изображения.

---

## Маршруты API

Проект поддерживает следующие API через Django Rest Framework:

- **Пользователи**
  - `POST /user/register/`: Регистрация пользователя
  - `POST /user/login/`: Авторизация пользователя
  - `GET /user/profile/`: Получение профиля пользователя
  - `PUT /user/profile/edit/`: Редактирование профиля пользователя

- **Объявления**
  - `GET /property/list/`: Список всех объявлений
  - `POST /property/create/`: Создание нового объявления
  - `PUT /property/edit/<id>/`: Редактирование объявления
  - `DELETE /property/delete/<id>/`: Удаление объявления

- **Бронирования**
  - `GET /booking/list/`: Список бронирований
  - `POST /booking/create/`: Создание нового бронирования

- **Аналитика**
  - `GET /user/analytics/`: Просмотр аналитики пользователя

Полная документация API доступна по следующим URL:
- Swagger: `/swagger/`
- Redoc: `/redoc/`

---

## Развертывание на продакшн

### Шаги для развертывания с использованием Docker:

1. Создайте файл `Dockerfile` для создания образа проекта.

2. Напишите `docker-compose.yml` для контейнеризации веб-приложения и базы данных.

3. Запустите Docker-контейнеры:
   ```bash
   docker-compose up --build
   ```

### Переменные окружения для продакшн:

- `SECRET_KEY`: Секретный ключ Django
- `DEBUG`: Установить в `False` для продакшн
- `DATABASE_URL`: URL базы данных (например, для PostgreSQL)
- `ALLOWED_HOSTS`: Хосты для развертывания
- Настройки для отправки email (SMTP сервер)

---

## Тестирование

Для запуска тестов:
```bash
python manage.py test
```

---

## Контрибуция

1. Форкните репозиторий.
2. Создайте ветку с новой функциональностью: `git checkout -b feature-branch`.
3. Сделайте коммит: `git commit -m 'Добавлена новая функциональность'`.
4. Сделайте пуш ветки: `git push origin feature-branch`.
5. Создайте Pull Request.

---

## Лицензия

Этот проект лицензирован под лицензией MIT — см. файл [LICENSE](LICENSE) для получения подробной информации.

---

## Авторы

- **Anar** — *Основной разработчик* — 

