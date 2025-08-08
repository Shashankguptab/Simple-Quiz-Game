#Quiz Game

def quiz_game():
    score = 0
    questions = {
        "What is the capital of France?": "paris",
        "Who developed Python programming language?": "guido van rossum",
        "What is 5 * 6?": "30",
        "Which planet is known as the Red Planet?": "mars",
        "What is the largest mammal on Earth?": "blue whale"
    }

    print("Welcome to the Quiz Game!")
    print("Type your answer and press Enter.\n")

    for question, answer in questions.items():
        user_answer = input(question + " ").strip().lower()
        if user_answer == answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {answer}\n")

    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent! You got all correct!")
    elif score >= len(questions) // 2:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")


quiz_game()
