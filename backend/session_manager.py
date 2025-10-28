class QuizSession:
    def __init__(self):
        self.score = 0
        self.total = 0

    def update(self, correct: bool):
        self.total += 1
        if correct:
            self.score += 1

    def get_score(self):
        return f"{self.score}/{self.total}"