from quiz_engine import generate_question, check_answer
from session_manager import QuizSession

def quiz_session():
    session = QuizSession()

    while True:
        question, options, answer = generate_question()

        print(f"\n📝 {question}")
        for key, val in options.items():
            print(f"{key}: {val}")

        user_choice = input("Your answer (A/B/C/D): ").strip().upper()
        feedback = check_answer(user_choice, answer)
        print(feedback)

        session.update(user_choice == answer)
        print(f"📊 Score: {session.get_score()}")

        again = input("Next question? (y/n): ").strip().lower()
        if again != "y":
            break

if __name__ == "__main__":
    quiz_session()