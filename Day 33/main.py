import datetime
import requests
from datetime import datetime
MY_LAT = 51.507351
MY_LNG = -0.127758


# # this is current location of ISS endpint http://api.open-notify.org/iss-now.json  # noqa
# response = requests.get("http://api.open-notify.org/iss-now.json")

# # raise_for_status method will return to the exception except for the success
# response.raise_for_status()

# # to fetch actual data
# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0

}
# https://api.sunrisesunset.io/json
# "https://api.sunrise-sunset.org/json"
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)  # noqa
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


time_now = datetime.now()

print(time_now.hour)
