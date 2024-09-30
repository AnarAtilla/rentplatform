const express = require('express');
const router = express.Router();

// Отправка отзыва
router.post('/new', (req, res) => {
    const reviewData = req.body;
    // Логика обработки отзыва
    res.json({ message: 'Отзыв отправлен', data: reviewData });
});

module.exports = router;