from flask import render_template

def home():
    return render_template("home.html")

def about():
    return render_template("about.html")

def rancher():
    return render_template("rancher.html")

def splunck():
    return render_template("splunck.html")

def newrelic():
    return render_template("newrelic.html")

def stash():
    return render_template("stash.html")

def infraconfig():
    return render_template("infraconfig.html")

def swagger():
    return render_template("swagger.html")

def sharepoint():
    return render_template("sharepoint.html")

def pipeline():
    return render_template("pipeline.html")