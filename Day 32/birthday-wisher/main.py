import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAL = "d26315258@gmail.com"
PASSWORD = "plgiikwdkkyhdgdq"

today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pd.read_csv("Day 32/birthday-wisher/birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}  # noqa


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Day 32/birthday-wisher/letter_templates/letter_{random.randint(1,3)}.txt"  # noqa
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")
