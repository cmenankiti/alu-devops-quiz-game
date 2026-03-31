import os
from flask import Flask, render_template, jsonify
import requests
from dotenv import load_dotenv

# 1. Load the .env file immediately
load_dotenv()

app = Flask(__name__)

# 2. Grab the Key and the URL
QUIZ_API_KEY = os.getenv('QUIZ_API_KEY')
QUIZ_URL = "https://quizapi.io/api/v1/questions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-questions')
def get_questions():
    # 3. Define the "Security Envelope" (Headers)
    headers = {
        'X-Api-Key': QUIZ_API_KEY
    }
    # 4. Define the "Request Options" (Params)
    params = {
        'limit': 10,
        'category': 'DevOps'
    }
    
    try:
        # 5. Make the request with BOTH Headers and Params
        response = requests.get(QUIZ_URL, headers=headers, params=params, timeout=8)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            # This helps you debug if the API key is rejected
            print(f"API Error: {response.status_code} - {response.text}")
            raise Exception("API Error")
            
    except Exception as e:
        print(f"Connection Error: {e}")
        # BAckup question if the API fails
        return jsonify([
            {
                "question": "What does 'CI' stand for in CI/CD?",
                "answers": {"answer_a": "Continuous Integration", "answer_b": "Code Indexing"},
                "correct_answers": {"answer_a_correct": "true"}
            }
        ])

if __name__ == '__main__':
    # Standard Flask port
    app.run(host='0.0.0.0', port=5000)
