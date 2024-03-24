from flask import Flask, request, render_template
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chat():
    message = request.form["message"]
    response = get_response(message)
    return response

if __name__ == "__main__":
    app.run(debug=True)
