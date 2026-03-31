from flask import Flask, render_template, jsonify, request
import requests
import os
import random
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

QUIZ_API_KEY = os.getenv("QUIZ_API_KEY")
QUIZ_URL = "https://quizapi.io/api/v1/questions"

# Global in-memory question pool
question_pool = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-questions")
def get_questions():
    global question_pool

    category = request.args.get("category", "DevOps")
    difficulty = request.args.get("difficulty", "")

    try:
        # Refill question pool if too small
        if len(question_pool) < 10:
            params = {
                "api_key": QUIZ_API_KEY,
                "limit": 50,
                "category": category
            }

            if difficulty:
                params["difficulty"] = difficulty

            response = requests.get(QUIZ_URL, params=params, timeout=10)
            response.raise_for_status()

            api_data = response.json()
            fetched_questions = api_data.get("data", [])

            if not fetched_questions:
                raise ValueError("No questions returned from API")

            # Keep only valid multiple choice questions
            cleaned_questions = []
            for q in fetched_questions:
                answers = q.get("answers", [])
                if isinstance(answers, list) and len(answers) >= 2:
                    valid_answers = [a for a in answers if a.get("text")]
                    if len(valid_answers) >= 2:
                        q["answers"] = valid_answers
                        cleaned_questions.append(q)

            if not cleaned_questions:
                raise ValueError("No usable questions returned from API")

            random.shuffle(cleaned_questions)
            question_pool = cleaned_questions

        selected_questions = question_pool[:10]
        question_pool = question_pool[10:]

        return jsonify(selected_questions)

    except Exception as e:
        print(f"Error fetching quiz questions: {e}")

        fallback_questions = [
            {
                "id": "fallback1",
                "text": "What does 'CI' stand for in CI/CD?",
                "category": "DevOps",
                "difficulty": "Easy",
                "answers": [
                    {"id": "a1", "text": "Continuous Integration", "isCorrect": True},
                    {"id": "a2", "text": "Code Indexing", "isCorrect": False},
                    {"id": "a3", "text": "Central Infrastructure", "isCorrect": False},
                    {"id": "a4", "text": "Code Injection", "isCorrect": False}
                ]
            },
            {
                "id": "fallback2",
                "text": "Which tool is commonly used for containerization?",
                "category": "Docker",
                "difficulty": "Easy",
                "answers": [
                    {"id": "b1", "text": "Docker", "isCorrect": True},
                    {"id": "b2", "text": "Jenkins", "isCorrect": False},
                    {"id": "b3", "text": "Ansible", "isCorrect": False},
                    {"id": "b4", "text": "Terraform", "isCorrect": False}
                ]
            },
            {
                "id": "fallback3",
                "text": "Which command initializes a Git repository?",
                "category": "Git",
                "difficulty": "Easy",
                "answers": [
                    {"id": "c1", "text": "git init", "isCorrect": True},
                    {"id": "c2", "text": "git start", "isCorrect": False},
                    {"id": "c3", "text": "git create", "isCorrect": False},
                    {"id": "c4", "text": "git new", "isCorrect": False}
                ]
            },
            {
                "id": "fallback4",
                "text": "Which file is used to define Docker services in Docker Compose?",
                "category": "Docker",
                "difficulty": "Medium",
                "answers": [
                    {"id": "d1", "text": "docker-compose.yml", "isCorrect": True},
                    {"id": "d2", "text": "Dockerfile", "isCorrect": False},
                    {"id": "d3", "text": "compose.json", "isCorrect": False},
                    {"id": "d4", "text": "docker.yml", "isCorrect": False}
                ]
            },
            {
                "id": "fallback5",
                "text": "Which Linux command shows the current directory?",
                "category": "Linux",
                "difficulty": "Easy",
                "answers": [
                    {"id": "e1", "text": "pwd", "isCorrect": True},
                    {"id": "e2", "text": "ls", "isCorrect": False},
                    {"id": "e3", "text": "cd", "isCorrect": False},
                    {"id": "e4", "text": "dir", "isCorrect": False}
                ]
            },
            {
                "id": "fallback6",
                "text": "Which command lists running Docker containers?",
                "category": "Docker",
                "difficulty": "Easy",
                "answers": [
                    {"id": "f1", "text": "docker ps", "isCorrect": True},
                    {"id": "f2", "text": "docker ls", "isCorrect": False},
                    {"id": "f3", "text": "docker list", "isCorrect": False},
                    {"id": "f4", "text": "docker show", "isCorrect": False}
                ]
            },
            {
                "id": "fallback7",
                "text": "Which tool is commonly used for CI/CD pipelines?",
                "category": "CI/CD",
                "difficulty": "Medium",
                "answers": [
                    {"id": "g1", "text": "Jenkins", "isCorrect": True},
                    {"id": "g2", "text": "Photoshop", "isCorrect": False},
                    {"id": "g3", "text": "Excel", "isCorrect": False},
                    {"id": "g4", "text": "WordPress", "isCorrect": False}
                ]
            },
            {
                "id": "fallback8",
                "text": "Which Linux command changes file permissions?",
                "category": "Linux",
                "difficulty": "Medium",
                "answers": [
                    {"id": "h1", "text": "chmod", "isCorrect": True},
                    {"id": "h2", "text": "chown", "isCorrect": False},
                    {"id": "h3", "text": "ls", "isCorrect": False},
                    {"id": "h4", "text": "grep", "isCorrect": False}
                ]
            },
            {
                "id": "fallback9",
                "text": "What does Kubernetes mainly help with?",
                "category": "Kubernetes",
                "difficulty": "Medium",
                "answers": [
                    {"id": "i1", "text": "Container orchestration", "isCorrect": True},
                    {"id": "i2", "text": "Photo editing", "isCorrect": False},
                    {"id": "i3", "text": "Spreadsheet management", "isCorrect": False},
                    {"id": "i4", "text": "Video rendering", "isCorrect": False}
                ]
            },
            {
                "id": "fallback10",
                "text": "Which command is used to clone a Git repository?",
                "category": "Git",
                "difficulty": "Easy",
                "answers": [
                    {"id": "j1", "text": "git clone", "isCorrect": True},
                    {"id": "j2", "text": "git copy", "isCorrect": False},
                    {"id": "j3", "text": "git pull", "isCorrect": False},
                    {"id": "j4", "text": "git start", "isCorrect": False}
                ]
            }
        ]

        # Optional filtering on fallback too
        filtered_fallback = [
            q for q in fallback_questions
            if (category.lower() in q.get("category", "").lower() or category == "DevOps")
            and (difficulty.lower() == q.get("difficulty", "").lower() or difficulty == "")
        ]

        if len(filtered_fallback) < 10:
            filtered_fallback = fallback_questions

        random.shuffle(filtered_fallback)
        return jsonify(filtered_fallback[:10])

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
