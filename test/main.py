from bs4 import BeautifulSoup
import requests
import smtplib
import os

# URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
URL = "https://www.amazon.in/Samsung-40-62cm-Dynamic-Graphite-NP960XFG-KC2IN/dp/B0BSH4MRWR/ref=sr_1_16?crid=3NEQSO36N807W&keywords=macbook%2Bair%2Bm2&qid=1699614795&sprefix=mac%2Caps%2C198&sr=8-16&th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}
THRESHOLD_PRICE = 200000

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
TO_ADDRESS = os.environ.get("MY_TO_MAIL_ADDRESS")

response = requests.get(URL,headers=HEADERS)
product_page = response.text

soup = BeautifulSoup(product_page,'lxml')

product_name = soup.find(name="span", id="productTitle").text.strip()  # type:ignore
price_text = soup.find(name="span", class_="a-price-whole").text.strip(".") # type:ignore
price = int(price_text.replace(",",""))

message = f"Subject:Amazon Price Alert\n\nProduct Name: {product_name}\nPrice: {price_text}\nPurchase Link: {URL}"

if price < THRESHOLD_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=PASSWORD
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRESS,
            msg=message
        )
