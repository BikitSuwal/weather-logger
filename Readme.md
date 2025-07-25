# 🌦️ Weather Logger Automation

A simple Python automation project to fetch current weather data and log it periodically. Ideal for learning Python scripting, APIs, and automation using GitHub Actions or the `schedule` library.

## 📌 Features

- Fetches real-time weather data using an API
- Logs weather details (temperature, condition, etc.) to a local file
- Automatically runs via:
  - GitHub Actions workflow (CI/CD)
  - Or locally using the `schedule` Python library

## 🚀 How It Works

- The `weather.py` script makes an API call (e.g., to OpenWeatherMap or wttr.in)
- Parses the data and logs it into `weather_log.txt` with timestamps
- Can be scheduled:
  - On GitHub via `.github/workflows/weather.yml`
  - Locally using a scheduler like `schedule` or `cron`

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install dependencies:

```bash
pip install -r requirements.txt
````

## 🧪 Usage

Run manually:

```bash
python weather.py
```

Or schedule using Python's `schedule` library:

```python
import schedule
import time

schedule.every().day.at("08:00").do(log_weather)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## ⚙️ GitHub Actions
Workflow file: `.github/workflows/weather.yml`
```yaml
name: Weather Logger

on:
  workflow_dispatch:
  schedule:
    - cron: '0 * * * *' # every hour

jobs:
  run-weather-logger:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run script
        run: python weather.py
```

## 📁 Output
All weather logs are saved in:

```
weather_log.txt
```

Each entry includes:
* Timestamp
* Temperatur
* Weather condition

## 📌 To-Do
* [ ] Add support for multiple cities
* [ ] Improve formatting of logs
* [ ] Add unit tests
* [ ] Deploy logs to a remote database or dashboard

Bikit Suwal
Part of my **#60DaysOfTech** journey – Day 35
Feel free to use or contribute!





