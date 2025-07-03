from flask import Flask, render_template, redirect, url_for
from forms import UserInfoForm

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for Flask-WTF

@app.route("/", methods=["GET", "POST"])
def index():
    form = UserInfoForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        return render_template("result.html", name=name, email=email)
    return render_template("form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
