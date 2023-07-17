from flask import Flask, render_template

app = Flask(__name__)

#Landing page
@app.route("/")
def landing_page():
    return render_template('landing_page.html')

@app.route("/auvo_15")
def auvo():
    return render_template('auvo_form.html')

@app.route("/chatshub_16")
def chats_hub():
    return render_template('chatshub_form.html')

#Ativar site
if __name__ == "__main__":
    app.run(debug=True)