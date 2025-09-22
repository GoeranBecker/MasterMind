from flask import Flask, render_template, redirect, url_for


app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route("/")
def home():
    return render_template("base.html")



if __name__ == "__main__":
    app.run(debug= True)