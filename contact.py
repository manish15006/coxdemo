from flask import render_template, request, redirect, flash, url_for
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()  # Ensure .env variables are loaded

def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        message = request.form["message"]

        smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.environ.get("SMTP_PORT", 587))
        smtp_username = os.environ.get("SMTP_USERNAME")
        smtp_password = os.environ.get("SMTP_PASSWORD")
        to_email = os.environ.get("TO_EMAIL")

        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        Message: {message}
        """

        msg = MIMEText(body)
        msg["Subject"] = f"Contact Form Submission: {subject}"
        msg["From"] = smtp_username
        msg["To"] = to_email

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, msg.as_string())
            server.quit()
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash("Failed to send message. Please try again later.", "danger")

        return redirect(url_for("contact"))
    return render_template("contact.html")