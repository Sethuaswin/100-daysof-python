import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
TO_ADDRESS = os.environ.get("MY_TO_MAIL_ADDRESS")

print(MY_EMAIL)
print(PASSWORD)
print(TO_ADDRESS)
