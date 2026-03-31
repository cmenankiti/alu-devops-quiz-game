# DevOps Training Center

## Overview
DevOps Training Center is a web-based quiz application designed to help users learn and practice DevOps concepts interactively.

The application fetches live technical questions from an external API and presents them in a simple quiz format. Users can answer questions, get instant feedback, track their score, and practice different categories and difficulty levels.

This project was developed as part of an API-based assignment and deployed across multiple servers with a load balancer.

---

## Purpose and Value
This application provides practical value by helping users:
- Practice DevOps interview questions
- Improve technical knowledge
- Learn through instant correction and repetition
- Interact with educational content in a simple and engaging way

Unlike gimmick applications, this project serves a real learning purpose.

---

## Features
- Fetches live quiz questions from an external API
- Supports category filtering
- Supports difficulty filtering
- Shows one question at a time
- Displays correct answers after wrong attempts
- Tracks score for each 10-question round
- Loads a new round after completion
- Randomizes answer order
- Includes fallback questions if the API is unavailable
- Includes a custom 404 error page

---

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **API Requests:** Requests
- **Environment Variables:** python-dotenv
- **Deployment:** Gunicorn, Nginx
- **Servers:** Web01, Web02, Load Balancer

---

## External API Used
This project uses **QuizAPI** to retrieve quiz questions.

- **API Provider:** QuizAPI
- **Website:** https://quizapi.io/
- **Documentation:** https://quizapi.io/docs/1.0/overview

### Attribution
Credit goes to the developers of QuizAPI for providing the quiz question data used in this application.

---

## Project Structure

```bash
alu-devops-quiz-game/
├── .env
├── .gitignore
├── __pycache__/
├── app.py
├── requirements.txt
└── templates/
    ├── 404.html
    └── index.html
