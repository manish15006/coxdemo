from flask import Flask, render_template
import views
import contact
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")  # Needed for flash messages

app.add_url_rule("/", "home", views.home)
app.add_url_rule("/about", "about", views.about)
app.add_url_rule("/rancher", "rancher", views.rancher)
app.add_url_rule("/splunck", "splunck", views.splunck)
app.add_url_rule("/newrelic", "newrelic", views.newrelic)
app.add_url_rule("/stash", "stash", views.stash)
app.add_url_rule("/infraconfig", "infraconfig", views.infraconfig)
app.add_url_rule("/swagger", "swagger", views.swagger)
app.add_url_rule("/sharepoint", "sharepoint", views.sharepoint)
app.add_url_rule("/contact", "contact", contact.contact, methods=["GET", "POST"])

# Keep only one definition for the /pipeline route
@app.route("/pipeline")
def pipeline():
    base_url = os.getenv("BASE_URL")
    endpoints = ["docker-branch", "feature-branch", "release-branch","Manoj"]
    return render_template("pipeline.html", base_url=base_url, endpoints=endpoints)

if __name__ == "__main__":
    app.run(debug=True)
