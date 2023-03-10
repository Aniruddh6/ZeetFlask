from flask import Flask,render_template

app=Flask(__name__)

@app.route("/bumper_sale")
def home():
    return "whatsapp karna"


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
