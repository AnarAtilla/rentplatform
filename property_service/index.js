const express = require('express');
const router = express.Router();

// Получение данных о собственности
router.get('/:id', (req, res) => {
    const propertyId = req.params.id;
    // Логика получения информации о собственности
    res.json({ message: 'Детали собственности', propertyId });
});

module.exports = router;