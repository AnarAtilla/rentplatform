const express = require('express');
const app = express();
const cors = require('cors');
const bodyParser = require('body-parser');

// Подключаем маршруты сервисов
const analytics = require('../analytics_service/index'); // Измените путь здесь
const booking = require('../booking_service/index');
const notifications = require('../notifications_service/index');
const property = require('../property_service/index');
const reviews = require('..//review_service/index');
const user = require('../user_service/index');

app.use(cors());
app.use(bodyParser.json());

// Настройка маршрутов
app.use('/api/analytics', analytics); // Убедитесь, что маршрут правильно подключен
app.use('/api/booking', booking);
app.use('/api/notifications', notifications);
app.use('/api/property', property);
app.use('/api/reviews', reviews);
app.use('/api/user', user);

// Запуск сервера
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Сервер запущен на http://localhost:${PORT}`);
});