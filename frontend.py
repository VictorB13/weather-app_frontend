from dotenv import load_dotenv
from flask import Flask, render_template_string, request
import requests
import os

load_dotenv()

app = Flask(__name__)

# אם רוצים אפשר להגדיר URL של backend דרך ENV
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5001")

CITIES = {
    "newyork": "New York",
    "sydney": "Sydney",
    "capetown": "Cape Town",
    "bangkok": "Bangkok"
}

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Weather Dashboard</title>
    <!-- Bootstrap + Google Fonts -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #73a5ff, #5477f5);
            min-height: 100vh;
            color: #fff;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            border: none;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: scale(1.05);
        }
        .btn-primary {
            background-color: #ffb347;
            border: none;
            transition: background 0.3s;
        }
        .btn-primary:hover {
            background-color: #ffcc70;
        }
        select.form-select {
            border-radius: 10px 0 0 10px;
        }
    </style>
</head>
<body>
<div class="container mt-5 text-center">
    <h1 class="mb-5 fw-bold">Weather Dashboard</h1>
    <form method="post" class="mb-4 d-flex justify-content-center">
        <div class="input-group w-50">
            <select class="form-select" name="city">
                {% for key, name in cities.items() %}
                    <option value="{{ key }}" {% if selected_city == key %}selected{% endif %}>{{ name }}</option>
                {% endfor %}
            </select>
            <button class="btn btn-primary" type="submit">Get Weather</button>
        </div>
    </form>

    {% if weather %}
    <div class="card mx-auto mt-4 p-4 shadow" style="width: 24rem;">
        <h4 class="fw-bold">{{ weather.city }}</h4>
        <p class="mb-1">🌡 Temperature: {{ weather.temperature }} °C</p>
        <p class="mb-1">☁ Description: {{ weather.description }}</p>
        <p class="mb-1">💧 Humidity: {{ weather.humidity }}%</p>
        <p>🌬 Wind: {{ weather.wind_speed }} m/s</p>
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    selected_city = None

    if request.method == "POST":
        selected_city = request.form.get("city")
        if selected_city in CITIES:
            try:
                response = requests.get(f"{BACKEND_URL}/weather/{selected_city}")
                if response.status_code == 200:
                    weather = response.json()
                else:
                    weather = {"city": CITIES[selected_city], "temperature": "N/A", "description": "Error fetching data",
                               "humidity": "N/A", "wind_speed": "N/A"}
            except Exception as e:
                weather = {"city": CITIES[selected_city], "temperature": "N/A", "description": f"Error: {e}",
                           "humidity": "N/A", "wind_speed": "N/A"}

    return render_template_string(HTML_TEMPLATE, cities=CITIES, weather=weather, selected_city=selected_city)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
