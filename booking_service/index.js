const express = require('express');
const router = express.Router();

// Создание бронирования
router.post('/new', (req, res) => {
    const bookingData = req.body;
    // Логика создания бронирования
    res.json({ message: 'Бронирование создано', data: bookingData });
});

module.exports = router;// Бронирование
