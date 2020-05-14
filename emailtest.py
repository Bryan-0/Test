import smtplib

sender = "Private Person <from@smtp.mailtrap.io>"
receiver = "A Test User <to@smtp.mailtrap.io>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("--------", "-------")
    server.sendmail(sender, receiver, message)