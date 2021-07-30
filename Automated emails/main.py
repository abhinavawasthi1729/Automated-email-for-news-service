import yagmail
import pandas
from news import Newsfeed
import datetime, time

df = pandas.read_excel('details.xlsx')

while True:
    if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 0:               #send email at particular time automatically
        for index, row in df.iterrows():
            news = Newsfeed(row['Interest'])
            content = news.get()

            email = yagmail.SMTP(user="abhinavawasthikvgn@gmail.com", password="meinemutter")
            email.send(to=row['Email'],
                        subject=f"Your {row['Interest']} news for today!",
                        contents=f"Hi {row['Name']}, See what's on about {row['Interest']} today.\n {content} \n Abhinav")

    time.sleep(60)