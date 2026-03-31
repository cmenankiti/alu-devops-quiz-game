import os
from flask import Flask, render_template, jsonify, request
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Use QuizAPI key from https://quizapi.io/
QUIZ_API_KEY = os.getenv('QUIZ_API_KEY')
QUIZ_URL = "https://quizapi.io/api/v1/questions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-questions')
def get_questions():
    params = {
        'apiKey': QUIZ_API_KEY,
        'limit': 10,
        'category': 'DevOps'
    }
    
    try:
        response = requests.get(QUIZ_URL, params=params, timeout=5)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            raise Exception("API Error")
    except Exception:
        # To make sure the application doesn't crash if API is down
        return jsonify([
            {
                "question": "What does 'CI' stand for in CI/CD?",
                "answers": {"answer_a": "Continuous Integration", "answer_b": "Code Indexing"},
                "correct_answers": {"answer_a_correct": "true"}
            }
        ])

@app.errorhandler(404)
def page_not_found(e):
    # This renders your custom 404.html template
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

