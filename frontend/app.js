const express = require("express");
const axios = require("axios");
const path = require("path");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

const API_URL = process.env.API_URL || "http://api:8000";

app.use(express.json());
app.use(express.static(path.join(__dirname, "views")));

const client = axios.create({
  baseURL: API_URL,
  timeout: 5000,
});

app.post("/submit", async (req, res) => {
  try {
    const response = await client.post("/jobs", {});

    res.json({
      job_id: response.data.job_id,
    });
  } catch (err) {
    console.error("API ERROR:", err.response?.data || err.message);

    res.status(502).json({
      error: "API unavailable",
      details: err.response?.data || err.message,
    });
  }
});

app.get("/status/:id", async (req, res) => {
  try {
    const response = await client.get(`/jobs/${req.params.id}`);
    res.json(response.data);
  } catch (err) {
    console.error("STATUS ERROR:", err.response?.data || err.message);

    res.status(502).json({
      error: "API unavailable",
      details: err.response?.data || err.message,
    });
  }
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});
