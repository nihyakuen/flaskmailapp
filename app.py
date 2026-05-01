from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        to = request.form["to"]
        subject = request.form["subject"]
        message = request.form["message"]

        try:
            server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
            server.login(login, password)

            msg = MIMEText(message, "plain", "utf-8")
            msg["Subject"] = subject
            msg["From"] = login
            msg["To"] = to

            server.send_message(msg)
            server.quit()

            return "Письмо отправлено!"

        except Exception as e:
            return f"Ошибка: {e}"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)