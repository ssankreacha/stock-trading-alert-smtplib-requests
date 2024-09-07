import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co | When STOCK price 🔺/🔻 by 5% between yesterday & day prior print("Get News").
av_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": " ",          # ENTER YOUR API KEY WITH & FROM THE API
}
av_response = requests.get(url="https://www.alphavantage.co/query", params=av_parameters)
av_status_code = av_response.status_code  # # Status = 200
tesla_stock_price_29 = float(av_response.json()["Time Series (60min)"]["2024-07-29 19:00:00"]["4. close"])  # yesterday
tesla_stock_price_26 = float(av_response.json()["Time Series (60min)"]["2024-07-26 19:00:00"]["4. close"])  # day before
percentage_change = (tesla_stock_price_29 - tesla_stock_price_26) / tesla_stock_price_29 * 100      # 5.0314 % 🔺
if percentage_change > 5:
    print("Get News!! ")


# STEP 2: Use https://newsapi.org | Instead of printing ("Get News"), Get first 3 news pieces for the COMPANY_NAME.
news_parameter = {
    "q": COMPANY_NAME,
    "from": 2024-7-29,
    "sortBy": "popularity",
    "apiKey": " "        # ENTER YOUR API KEY WITH & FROM THE API
}
news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameter)
news_status_code = news_response.status_code    # Status = 200
# News Articles 1, 2, 3 -> Author, Title, Descriptions
author_1 = news_response.json()["articles"][0]["author"]
title_1 = news_response.json()["articles"][0]["title"]
desc_1 = news_response.json()["articles"][0]["description"]
author_2 = news_response.json()["articles"][1]["author"]
title_2 = news_response.json()["articles"][1]["title"]
desc_2 = news_response.json()["articles"][1]["description"]
author_3 = news_response.json()["articles"][2]["author"]
title_3 = news_response.json()["articles"][2]["title"]
desc_3 = news_response.json()["articles"][2]["description"]


# STEP 3: Use Email: Send separate message with percentage change and each article's title and description to email.
sender_email = " "      # Enter your email
sender_password = " "  # Passkey found with your email provider
recipient_email = " "  # recipient email

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    connection.sendmail(from_addr=sender_email,                     # Email 1
                        to_addrs=recipient_email,
                        msg="Subject:Stock Market Update\n\n"f"🔺{percentage_change}\n{author_1}\n{title_1}\n{desc_1}")
    connection.sendmail(from_addr=sender_email,                     # Email 2
                        to_addrs=recipient_email,
                        msg="Subject:Stock Market Update\n\n"f"🔺{percentage_change}\n{author_2}\n{title_2}\n{desc_2}")
    connection.sendmail(from_addr=sender_email,                     # Email 3
                        to_addrs=recipient_email,
                        msg="Subject:Stock Market Update\n\n"f"🔺{percentage_change}\n{author_3}\n{title_3}\n{desc_3}")
    connection.close()
