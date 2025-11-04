from flask import *
from flask import Flask, render_template
from pathlib import Path
import random

app = Flask(__name__)

question_file = Path(app.static_folder) / "questions.txt"
data_dict = {}

if question_file.exists():
    with question_file.open("r", encoding="utf-8") as file:
        for line in file:
            key, value = (line.split("|", 1) + [""])[:2]
            data_dict[key.strip()] = value.strip()
else:
    print(f"Warning: questions file not found at {question_file}")

@app.route("/", methods=['GET', 'POST'])
def home():
    question = None
    if request.method == 'POST':
        if data_dict:
            question = random.choice(list(data_dict.keys()))
    return render_template("base.html", question=question)

if __name__ == "__main__":
    app.run(debug=True)