from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from backend.quiz_engine import generate_question
import os

app = FastAPI()

# Serve frontend via symlinked static folder
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "static")), name="static")


@app.get("/question")
def get_question():
    print("🔍 /question endpoint hit")
    question, options, answer = generate_question()
    return JSONResponse({
        "question": question,
        "options": options,
        "answer": answer

    })
