const express = require('express');
const router = express.Router();

// Получение аналитических данных
router.get('/data', (req, res) => {
    // Здесь должна быть логика получения аналитических данных
    res.json({ message: 'Аналитические данные' });
});

module.exports = router;// Аналитический сервис
