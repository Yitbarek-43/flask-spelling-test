# spelling_test_web.py

from flask import Flask, render_template_string, request

app = Flask(__name__)

# List of words for the test
WORDS = [
    "protective", "armor", "arrive", "exhausting", "scared",
    "impressed", "battle", "emperor", "troops", "appeared",
    "traveled", "wide", "thank", "you", "watching"
]

# HTML template (all in one file)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Spelling Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f7f9fb;
            color: #333;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            color: #004aad;
        }
        form {
            margin-top: 30px;
        }
        input[type=text] {
            padding: 10px;
            width: 250px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            background: #004aad;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #00337a;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
        }
        .correct { color: green; }
        .incorrect { color: red; }
    </style>
</head>
<body>
    <h1>🧠 Online Spelling Test</h1>
    <p>Spell the words correctly and click "Submit".</p>
    <form method="POST">
        {% for word in words %}
            <div>
                <label><strong>Word {{ loop.index }}:</strong></label><br>
                <input type="text" name="word{{ loop.index }}" placeholder="Type spelling here">
            </div><br>
        {% endfor %}
        <button type="submit">Submit</button>
    </form>

    {% if results %}
        <div class="result">
            <h2>Results:</h2>
            {% for res in results %}
                <p class="{{ 'correct' if res.correct else 'incorrect' }}">
                    {{ loop.index }}. {{ res.word }} → 
                    {% if res.correct %} ✅ Correct {% else %} ❌ Correct spelling: {{ res.correct_word }} {% endif %}
                </p>
            {% endfor %}
            <h3>Final Score: {{ score }}/{{ total }}</h3>
        </div>
    {% endif %}
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
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=False)
