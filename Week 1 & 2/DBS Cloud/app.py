from flask import Flask, render_template, request

app = Flask(__name__) ## loading user credentials

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        return (render_template("index.html", result = 90.2 - (50.6*rates)))
    else:
        return(render_template("index.html", result = "waiting"))

if __name__ == "__main__":
    app.run()