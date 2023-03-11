from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "DIvsatun 5 min kadhna fakt mazhya sathih aani whatsapp karna, 5 min bolu tari, kal tuzhya sobat 2 min chat karun mi evadha khush zhalelo tula sangu nahi shakat mi"


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
