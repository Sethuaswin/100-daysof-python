import smtplib
import datetime as dt
import random


MY_EMAL = "your-email"
PASSWORD = "your-password"
TO_MAIL = "sender-email"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 4:
    with open("Day 32/motivation-mail/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAL,
            to_addrs=TO_MAIL,
            msg=f"Subject:Friday Motivation\n\n{quote}"
        )
