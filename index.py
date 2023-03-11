from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "Mala whatsapp kar na, fakt 5 min bolu, fakt 5 min, samja aata possibble hot nasel tar mala ek time sang ki mi ya timela free asen tevha mi message karen tevha bolu 5 min, please he sang karan kal mi 2 paryant ratri thamblelo ki hila aata tari jamel bolayla karan tula 11 vajta possible navta"


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
