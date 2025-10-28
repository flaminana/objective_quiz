let currentAnswer = "";
let score = 0;
let total = 0;

function loadQuestion() {
  fetch("/question")
    .then(res => res.json())
    .then(data => {
      document.getElementById("question").innerText = data.question;
      const buttons = document.querySelectorAll("#options button");
      const keys = ["A", "B", "C", "D"];
      keys.forEach((key, i) => {
        buttons[i].innerText = `${key}: ${data.options[key]}`;
      });
      currentAnswer = data.answer;
    });
}

function submitAnswer(choice) {
  total++;
  if (choice === currentAnswer) {
    score++;
    document.getElementById("feedback").innerText = "✅ Correct!";
  } else {
    document.getElementById("feedback").innerText = `❌ Incorrect. Correct answer: ${currentAnswer}`;
  }
  document.getElementById("score").innerText = `Score: ${score}/${total}`;
  setTimeout(loadQuestion, 2000);
}

window.onload = loadQuestion;