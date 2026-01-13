##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import os

import pandas as pd
from random import *
import smtplib
from dotenv import load_dotenv
load_dotenv()
my_email =os.environ.get("MY_EMAIL")
password =os.environ.get("PASSWORD")


letter_list = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
letter = choice(letter_list)



def send_mail(user_email,user_name,sent_letter):
  with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    with open(sent_letter) as f:
       file_content = f.read()
       file_content = file_content.replace("[NAME]",user_name)


    connection.sendmail(
        from_addr=my_email,
        to_addrs=user_email,
        msg=f"{file_content},"

     )

tdy = dt.datetime.today()
today = tdy.day
this_month = tdy.month


data = pd.read_csv("birthdays.csv")
for index, row in data.iterrows():

    month = row["month"]
    day = row["day"]
    name = row["name"]
    email = row["email"]



    if today == day and this_month == month:
        if name == "Rosh":
            letter_r = "letter_templates/rosh.txt"
            send_mail(email, name, letter_r)
        elif name=="Harish Bot":
            letter_h = "letter_templates/harish.txt"
            send_mail(email, name, letter_h)
        else:
           send_mail(email,name,letter)




