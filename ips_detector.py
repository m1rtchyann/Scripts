#!/usr/bin/env python3
import sys
import smtplib
import re
import schedule
import time
from termcolor import cprint, colored

def get_banned_ips(log_file):
    banned_ip = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'^.*? Ban (?P<ip>\d+\.\d+\.\d+\.\d+)$', line)
            if match:
                ip = match.group('ip')
                if ip not in banned_ip:
                    banned_ip.append(ip)
    return banned_ip

def send_email(banned_ip):
    sender_email = 'sender@gmail.com'
    sender_password = 'app-password-code-from-gmail'
    recipient_email = 'recipient@gmail.com'
    subject = 'Fail2ban Banned IPs'
    message = "The following IP addresses are banned by Fail2Ban:\n\n" + "\n".join(banned_ip)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{message}")

def job():
    log_file = "/var/log/fail2ban.log"
    banned_ip = get_banned_ips(log_file)
    if banned_ip:
        send_email(banned_ip)

if __name__ == "__main__":
    cprint("WELCOME TO OUR IPS DETECTOR", "green", attrs=["bold"])
    print("Looking for banned ip addresses...")
    job()

    cprint("Please, check your email", "green", attrs=["bold"])
    print("\033[3mIf there is no message, everything is fine\033[0m")

    # Schedule the job to run every 10 minutes
    schedule.every(30).minutes.do(job)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)