# spelling_test.py

def spelling_test():
    print("🧠 Welcome to the Spelling Test!")
    print("You will be asked to spell a few words. Type your answers carefully.\n")

    # List of words for the test
    words = [
        "protective", "armor", "arrive", "exhausting", "scared",
        "impressed", "battle", "emperor", "troops", "appeared",
        "traveled", "wide", "thank", "you", "watching"
    ]

    score = 0

    for i, word in enumerate(words, 1):
        print(f"Word {i}: Please spell this word:")
        user_answer = input("👉 Your answer: ").strip().lower()

        if user_answer == word:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct spelling is '{word}'.\n")

    print("📊 Test completed!")
    print(f"Your final score: {score}/{len(words)}")

    if score == len(words):
        print("🏆 Excellent! You spelled all words correctly.")
    elif score >= len(words) * 0.7:
        print("👍 Good job! A little more practice and you’ll be perfect.")
    else:
        print("💪 Keep practicing! You can improve next time.")


# Run the test
if __name__ == "__main__":
    spelling_test()
