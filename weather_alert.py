import os
import requests
import smtplib
from email.message import EmailMessage

API_KEY = os.environ["OWM_API_KEY"]
CITY = os.environ["CITY"]

SMTP_SERVER = os.environ["SMTP_SERVER"]
SMTP_PORT = int(os.environ["SMTP_PORT"])
EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
ALERT_TO = os.environ["ALERT_TO"]

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)

response = requests.get(url, timeout=30)
response.raise_for_status()

data = response.json()

temp = data["main"]["temp"]
condition = data["weather"][0]["main"]
forecast_url = (
    f"https://api.openweathermap.org/data/2.5/forecast"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)

forecast_response = requests.get(forecast_url, timeout=30)
forecast_response.raise_for_status()

forecast_data = forecast_response.json()

rain_predicted = False

for item in forecast_data["list"]:
    weather = item["weather"][0]["main"] 
if rain_predicted:
    send_alert = True
    reasons.append("Rain predicted in forecast")
print(f"City: {CITY}")
print(f"Temperature: {temp}°C")
print(f"Condition: {condition}")
print(f"Rain predicted: {rain_predicted}")

send_alert = False
reasons = []

if temp > 35:
    send_alert = True
    reasons.append(f"Temperature is {temp:.1f}°C")

if rain_predicted:
    send_alert = True
    reasons.append("Rain predicted in forecast")

if send_alert:
    msg = EmailMessage()
    msg["Subject"] = f"Weather Alert for {CITY}"
    msg["From"] = EMAIL_USER
    msg["To"] = ALERT_TO

    msg.set_content(
        "Weather Alert\n\n" + "\n".join(reasons)
    )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Email alert sent.")
else:
    print("No alert needed.")
