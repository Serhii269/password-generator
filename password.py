from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    error = ""
    if request.method == "POST":
        try:
            length = int(request.form["length"])
            if length < 6:
                error = "Password length should be at least 6 characters."
            else:
                password = generate_password(length)
        except ValueError:
            error = "Please enter a valid number."
    return render_template("index.html", password=password, error=error)

if __name__ == "__main__":
    app.run(debug=True)

