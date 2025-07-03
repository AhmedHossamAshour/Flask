from flask import Flask, render_template, redirect, url_for
from forms import NameForm

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/form", methods=["GET", "POST"])
def form():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for('greet', username=name))
    return render_template("form.html", form=form)

@app.route("/greet/<username>")
def greet(username):
    return f"Hello, {username}!"

if __name__ == "__main__":
    app.run(debug=True)
