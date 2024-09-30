// Пользователи
const express = require('express');
const router = express.Router();

// Регистрация нового пользователя
router.post('/register', (req, res) => {
    const userData = req.body;
    // Логика регистрации пользователя
    // Здесь вы можете добавить код для сохранения пользователя в базу данных
    res.json({ message: 'Пользователь зарегистрирован', data: userData });
});

// Получение данных пользователя (пример)
router.get('/data', (req, res) => {
    // Здесь должна быть логика для получения данных пользователя
    // Например, получение данных из базы данных
    res.json({ message: 'Данные пользователя', data: { id: 1, name: 'John Doe' } });
});

module.exports = router;