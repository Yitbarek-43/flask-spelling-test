from flask import Flask, render_template_string, request
import webbrowser

app = Flask(__name__)

# ✅ Updated words (excluded "thank", "you", and "watching")
WORDS = [
    "protective", "armor", "arrive", "exhausting", "scared",
    "impressed", "battle", "emperor", "troops", "appeared",
    "traveled", "wide"
]

# 🎨 HTML template with built-in text-to-speech via JavaScript
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Spelling Test with Voice</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f6ff;
            text-align: center;
            margin: 40px;
        }
        h1 {
            color: #004aad;
        }
        button {
            background-color: #004aad;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #00337a;
        }
        input[type=text] {
            width: 250px;
            padding: 8px;
            margin: 5px;
            border-radius: 5px;
            border: 1px solid #aaa;
        }
        .result {
            margin-top: 20px;
        }
        .correct { color: green; }
        .incorrect { color: red; }
    </style>
</head>
<body>
    <h1>🧠 Online Spelling Test (with Voice)</h1>
    <p>Click 🔊 to hear the word, then type the correct spelling below.</p>
    <form method="POST">
        {% for word in words %}
            <div>
                <label><strong>Word {{ loop.index }}</strong></label><br>
                <button type="button" onclick="speak('{{ word }}')">🔊 Play Word</button><br>
                <input type="text" name="word{{ loop.index }}" placeholder="Type spelling here"><br><br>
            </div>
        {% endfor %}
        <button type="submit">Submit</button>
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
            const utterance = new SpeechSynthesisUtterance(word);
            utterance.lang = 'en-US';
            speechSynthesis.speak(utterance);
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
