from flask import Flask, render_template_string, request
import webbrowser

app = Flask(__name__)

# List of words
WORDS = [
    "protective", "armor", "arrive", "exhausting", "scared",
    "impressed", "battle", "emperor", "troops", "appeared",
    "travelled", "wide"
]

# HTML template with pronunciation
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Spelling Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            text-align: center;
            margin-top: 30px;
        }
        h1 {
            color: #004aad;
        }
        button {
            background-color: #004aad;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            margin-top: 5px;
        }
        button:hover {
            background-color: #00337a;
        }
        input[type=text] {
            width: 220px;
            padding: 6px;
            margin: 5px;
            border-radius: 5px;
            border: 1px solid #aaa;
        }
        .result { margin-top: 20px; font-size: 16px; }
        .correct { color: green; }
        .incorrect { color: red; }
    </style>
</head>
<body>
    <h1>🧠 Online Spelling Test</h1>
    <p>Click 🔊 to hear the word, then type the spelling below.</p>

    <form method="POST">
        {% for word in words %}
            <div>
                <label><strong>Word {{ loop.index }}</strong></label><br>
                <button type="button" onclick="speak('{{ word }}')">🔊 Play Word</button><br>
                <input type="text" name="word{{ loop.index }}" placeholder="Type spelling here"><br><br>
            </div>
        {% endfor %}
        <button type="submit">Submit Answers</button>
    </form>

    {% if results %}
        <div class="result">
            <h2>Results:</h2>
            {% for res in results %}
                <p class="{{ 'correct' if res.correct else 'incorrect' }}">
                    {{ loop.index }}. You wrote: <strong>{{ res.word }}</strong> —
                    {% if res.correct %}✅ Correct{% else %}❌ Correct spelling: {{ res.correct_word }}{% endif %}
                </p>
            {% endfor %}
            <h3>Final Score: {{ score }}/{{ total }}</h3>
        </div>
    {% endif %}

    <script>
        function speak(word) {
            const utter = new SpeechSynthesisUtterance(word);
            utter.lang = 'en-US';
            speechSynthesis.speak(utter);
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def spelling_test():
    results = []
    score = 0

    if request.method == "POST":
        for i, correct_word in enumerate(WORDS, 1):
            user_word = request.form.get(f"word{i}", "").strip().lower()
            is_correct = user_word == correct_word
            if is_correct:
                score += 1
            results.append({
                "word": user_word if user_word else "(blank)",
                "correct_word": correct_word,
                "correct": is_correct
            })

    return render_template_string(HTML_TEMPLATE,
                                  words=WORDS if not results else [],
                                  results=results,
                                  score=score,
                                  total=len(WORDS))

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=False)
