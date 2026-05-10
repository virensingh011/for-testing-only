const express = require("express");
const cors = require("cors");

const app = express();
const port = process.env.PORT || 10000;
const openWeatherKey = process.env.OPENWEATHER_API_KEY;

app.use(cors());

app.get("/health", (_req, res) => {
  res.json({ ok: true, service: "aegis-atlas-api" });
});

app.get("/api/usgs/earthquakes", async (_req, res) => {
  try {
    const response = await fetch("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson");
    const data = await response.json();
    res.json(data);
  } catch (error) {
    res.status(502).json({ error: "USGS request failed", detail: error.message });
  }
});

app.get("/api/weather", async (req, res) => {
  if (!openWeatherKey) {
    res.status(503).json({ error: "OPENWEATHER_API_KEY is not configured" });
    return;
  }
  const lat = req.query.lat || "28.6139";
  const lon = req.query.lon || "77.2090";
  try {
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${openWeatherKey}&units=metric`;
    const response = await fetch(url);
    const data = await response.json();
    res.json(data);
  } catch (error) {
    res.status(502).json({ error: "OpenWeatherMap request failed", detail: error.message });
  }
});

app.listen(port, () => {
  console.log(`Aegis Atlas API listening on ${port}`);
});
