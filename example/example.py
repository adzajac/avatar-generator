import sys
sys.path = [".."] + sys.path

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, validators
from random import random
from avatargenerator import avatargenerator as ag


app = Flask(__name__)
app.config["SECRET_KEY"] = "ower-ads34-tndf-poe"


# ---------- model -----------

class User:
    first_name = ""
    second_name = ""
    img_path = ""

user = User()


# ---------- view -----------

@app.route("/", methods=["post","get"])
def index():
    form = ExampleRegistrationForm()
    if form.validate():
        user.first_name = form.first_name.data
        user.second_name = form.second_name.data
        user.img_path = ag.generateLetterAvatar(user.first_name, user.second_name, size=512, dir_path="static/generated_avatars/")
        return redirect(url_for("success"))
    return render_template("registration.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html", user=user)
           

# ---------- other -----------

class ExampleRegistrationForm(FlaskForm):
    first_name = StringField("First Name (required)", [validators.InputRequired()])
    second_name = StringField("Second Name")
    submit = SubmitField("Register")


