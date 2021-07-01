from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tests")
def tests():
    return render_template("Tests.html")

@app.route("/applications")
def applications():
    return render_template("applications.html")

@app.route("/programmer+application")
def prog_app():
    return render_template("prog_app.html")

if __name__ == "__main__":
    app.run()
