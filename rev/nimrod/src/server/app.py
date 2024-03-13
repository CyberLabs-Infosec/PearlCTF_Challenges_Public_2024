from flask import Flask
from flask import render_template, send_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/calc.elf", methods=["GET"])
def return_file():
    return send_file("calc.elf")

@app.route("/record", methods=["POST"])
def record():
    return "Information recieved"

if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=False)