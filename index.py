from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "Mala whatsapp kar na, fakt 5 min bolu, fakt 5 min"


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
