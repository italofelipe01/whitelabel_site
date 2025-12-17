from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def landing_page():
    return render_template('landing_page.html')

@main.route("/auvo_15")
def auvo():
    return render_template('auvo_form.html')

@main.route("/chatshub_16")
def chats_hub():
    return render_template('chatshub_form.html')
