import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "KUB50LVB4P57WARI"
NEWS_API_KEY = "de2af9c0b3204fae891bf4d2bc199c2e"

# twilio credentials
account_sid = "ACf050f9225a98d4092caac525efd4c985"
auth_token = "4199a98ca607193ec110e8cbcbc84ada"

# # STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").  # noqa

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]  # noqa
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [values for key, values in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp  # noqa
differce = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)  # noqa

up_down = None
if differce > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.  # noqa
diff_percent = round((differce/float(yesterday_closing_price)) * 100)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    # # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.   # noqa

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.  # noqa

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation  # noqa
    three_articles = articles[:3]

    # # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.  # noqa

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.  # noqa
    formatted_articles = [f"{STOCK_NAME}: {up_down} {diff_percent}% \nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]  # noqa
    print(formatted_articles)
# TODO 9. - Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12052365343',
            to='+919597169363',
            )
