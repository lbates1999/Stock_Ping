#stock notifications
#using Alpha Vantage API
import requests
from datetime import datetime
from tkinter import *
from time import time, ctime
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content


BLUE = "#4392F1"
GREY = "#E7F0FF"
WHITE = "#ECE8EF"
BLACK = "#252424"
RED = "#DC493A"

def button_clicked():
    return True





t = time()
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")
#form_date = (f"{formatted_date}")
form_date = '2024-08-13'

window =  Tk()
window.geometry("400x300")
window.title("StockPing")
window.configure(bg=WHITE)

#title
title = Label(text="Enter the Ticker Symbol for the stock you want updates for:", fg=BLACK, bg=WHITE, font=("arial", 10, "bold"))
title.grid(column=2, row=0)
ticker_entry = Entry()
ticker_entry.grid(column=2, row=2)
#email info
email_request = Label(text="Enter your email to send updates too", fg=BLACK, bg=WHITE, font=("arial", 10, "bold"))
email_request.grid(column=2, row=3)
email_entry = Entry()
email_entry.grid(column=2, row=4)
#frequency

freq_option = Label(text="When do you want to be notified?", fg=BLACK, bg=WHITE, font=("arial", 10, "bold"))
freq_option.grid(column=2, row=5)
options = ["Opening", "Closing"]
var = StringVar(window)
var.set(options[0])







dropdown = OptionMenu(window, var, *options)
dropdown.config(bg=WHITE, fg=BLACK, font=("Arial", 10))
dropdown.grid(column=2, row=6, sticky=W)

submit_button = Button(text="Submit", command=button_clicked)
submit_button.grid(column=2, row=7)


API_KEY = "Z3UI2C2K7N3KP75U"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'

input_function= (f"function=TIME_SERIES_DAILY")
input_symbol = (f"&symbol={ticker_entry}")
api_key_url = (f"&apikey={API_KEY}")
sending_url = (f"'{url}{input_function}{input_symbol}{api_key_url}'")

run_url = (sending_url)
r = requests.get(url)
data = r.json()


opening_price = data["Time Series (Daily)"][form_date]["1. open"]
price = round(float(opening_price), 2)
#print(f"The opening price for {ticker_input_2} is ${price}0")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

while True:
    if current_time == "10:00:00":
        sg = sendgrid.SendGridAPIClient(api_key='')
        from_email = Email("stockpingapi@gmail.com")
        to_email = To(f"{email_entry}")
        subject = (f"{ticker_entry} UPDATE")
        content = Content("text/plain", f"The opening price for {ticker_entry} is ${price}0")
        mail = Mail(from_email, to_email, subject, content)
    else:
        break


window.mainloop()
