import requests
from twilio.rest import Client

# openweathermap credentials
API_KEY = "wefowiefboiewfbowiefboiwefboiwe"
LAT = 51.51
LNG = -0.12
CITY = "London,uk"

# twilio credentials
account_sid = "Aasdyas77asa7tda7dtas77asd7asd7sa"
auth_token = "eb8be98g9e8rfw98efw8fw9PEFP9WEF"

# Example API Call - https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=9593ea54dd0f411f02d61e69285c2d98  # noqa
# https://api.openweathermap.org/data/2.5/onecall?lat=51.51&lon=-0.12&appid=9593ea54dd0f411f02d61e69285c2d98
# https://api.openweathermap.org/data/2.5/forecast?q=London,uk&appid=9593ea54dd0f411f02d61e69285c2d98

parameters = {
    "q": CITY,
    "appid": API_KEY,
    'units': 'metric'
}
# one_call_params = {
#     "lat": LAT,
#     "lon": LNG,
#     "appid": API_KEY
# }
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
    )
response.raise_for_status()
weather_data = response.json()
# getting first days of data
weather_slice = weather_data['list'][:9]

will_rain = False

for daily_data in weather_slice:
    condition_code = daily_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="There may down pour in coming days keep an Umbrella ☔ in bag ",
        from_='+12052365343',
        to='+919597169363'
        )
    print(message.status)
