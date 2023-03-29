import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day = now.weekday()
my_email = "rakshitdabral427@gmail.com"


if day == 2:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="mdbcskkjdveqxjsz")

        connection.sendmail(from_addr=my_email,
                            to_addrs="rakshitdabral1@gmail.com",
                            msg=f"Subject:MotivationShit\n\n{quote}")







