from ollama_client import query_ollama

def generate_question(topic="Basic beginner A1 German grammar and vocabulary"):
    prompt = (
        f"Create a multiple-choice question on {topic}. "
        "Format:\nQuestion: ...\nA: ...\nB: ...\nC: ...\nD: ...\nAnswer: ..."
    )
    raw = query_ollama(prompt)
    return parse_question(raw)

def parse_question(raw: str):
    lines = raw.split("\n")
    question = ""
    options = {}
    answer = ""

    for line in lines:
        line = line.strip()
        if line.lower().startswith("question:"):
            question = line.split(":", 1)[1].strip()
        elif line.startswith("A:") or line.startswith("A)"):
            options["A"] = line.split(":", 1)[1].strip()
        elif line.startswith("B:") or line.startswith("B)"):
            options["B"] = line.split(":", 1)[1].strip()
        elif line.startswith("C:") or line.startswith("C)"):
            options["C"] = line.split(":", 1)[1].strip()
        elif line.startswith("D:") or line.startswith("D)"):
            options["D"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("answer:"):
            answer_line = line.split(":", 1)[1].strip()
            if answer_line.startswith(("A)", "B)", "C)", "D)")):
                answer = answer_line[0]
            elif answer_line[0] in ("A", "B", "C", "D"):
                answer = answer_line[0]

    return question, options, answer

def check_answer(user_choice: str, correct_answer: str) -> str:
    if user_choice.upper() == correct_answer:
        return "✅ Correct!"
    else:
        return f"❌ Incorrect. The correct answer was {correct_answer}."