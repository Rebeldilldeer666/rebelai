const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/health', (req, res) => {
    res.status(200).json({ status: "online", engine: "Rebel AI Master Core", timestamp: new Date().toISOString() });
});

app.post('/v1/integrate/universal/:platform', (req, res) => {
    const { platform } = req.params;
    res.status(200).json({ success: true, platform, message: "Webhook synchronized successfully." });
});

app.listen(PORT, () => {
    console.log(`===============================================`);
    console.log(`🚀 INSTANT ENGINE OPERATIONAL & ONLINE`);
    console.log(`Local Dashboard URL: http://localhost:${PORT}/health`);
    console.log(`Universal Webhook Path: /v1/integrate/universal/:platform`);
    console.log(`===============================================`);
});
