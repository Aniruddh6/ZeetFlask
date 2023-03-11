from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "Whatsapp karna free zhalis ki \n5 min bolu \nkal tuzhya sobat 2 min chat karun mi evadha khush zhalelo tula sangu nahi shakat mi"


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
