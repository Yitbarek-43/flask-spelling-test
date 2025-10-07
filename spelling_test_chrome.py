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
            answer = request.form.get(f"word{i}", "").strip().lower()
            if answer == word.lower():
                score += 1
        result = f"You got {score} out of {len(words)} correct!"
    return render_template("index.html", words=words, result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
