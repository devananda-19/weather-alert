import os
import requests

API_KEY = os.environ["OWM_API_KEY"]
CITY = os.environ["CITY"]

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)

response = requests.get(url)
response.raise_for_status()

data = response.json()

temp = data["main"]["temp"]
condition = data["weather"][0]["main"]

print(f"City: {CITY}")
print(f"Temperature: {temp}°C")
print(f"Condition: {condition}")

if temp > 35:
    print("ALERT: Temperature exceeds 35°C")

if condition.lower() == "rain":
    print("ALERT: Rain detected")
