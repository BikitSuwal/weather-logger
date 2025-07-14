import requests
from datetime import datetime

def fetch_weather():
    try:
        response = requests.get('https://wttr.in/Kathmandu?format=%t')
        if response.status_code == 200:
            weather = response.text.strip()
            print(f"{datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}: {weather}")
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print("Error fetching weather data:", e)

if __name__ == "__main__":
    fetch_weather()