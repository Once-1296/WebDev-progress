// index.js
const express = require('express');
const app = express();
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(express.json());

// In-memory "database"
let users = [];

// GET route
app.get('/users', (req, res) => {
    res.json({
        message: 'List of users',
        data: users
    });
});

// POST route
app.post('/users', (req, res) => {
    const { name, email } = req.body;

    if (!name || !email) {
        return res.status(400).json({ error: 'Name and email are required' });
    }

    const newUser = { id: users.length + 1, name, email };
    users.push(newUser);

    res.status(201).json({
        message: 'User added successfully',
        user: newUser
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
