from flask import Flask, render_template, request

app = Flask(__name__)

# List of spelling words
words = [
    "protective", "armor", "arrive", "exhausting",
    "scared", "impressed", "battle", "emperor",
    "troops", "appeared", "travelled", "wide"
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        score = 0
        for i, word in enumerate(words):
            answer = request.form.get(f"word{i}", "").strip().lowe
