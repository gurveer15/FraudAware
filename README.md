# FraudAware

 A Flask-based web app to detect and raise awareness about financial scam messages using interactive quizzes and custom message analysis.

---

## Features

- **Quiz Mode** – Learn to identify real vs. scam messages with instant feedback and explanations.
- **Custom Message Checker** – Paste any message to instantly evaluate its risk using a keyword-based logic engine.
- **Real-Time Analysis** – Dynamic logic that scores based on suspicious vs. safe keywords.
- **Built-in Database** – Quiz questions and keyword data managed via MySQL for reliability and extensibility.

---

## Inspiration

With rising cases of digital fraud, people often fall for scam messages disguised as real ones. We built **FraudAware** to help users differentiate between safe and scam messages through an interactive and educational experience.

---

## What I Learned

- Implementing Flask for web routing and session management
- Structuring databases and executing SQL queries from Python
- Handling user input and POST/GET logic
- Using Git and GitHub for version control and collaboration

---

## Challenges Faced

- Designing a scoring system that feels intuitive yet secure
- Avoiding false positives in message analysis
- Structuring the database schema to include explanations
- Debugging Flask session issues and SQL connectivity

---

## Accomplishments That I am Proud Of

- Built a complete educational web app in a short time
- Developed a flexible quiz system with database-backed messages
- Pushed the project to GitHub and documented it professionally

---

## Built With

- Python (Flask)
- MySQL
- HTML + CSS
- CapCut (for demo video editing)

---

## Project Structure

```
FraudAware/
├── app.py
├── FraudAware.sql
├── static/
│ └── style.css
├── templates/
│ ├── index.html
│ ├── quiz.html
│ ├── feedback.html
│ └── check.html

```
---

## How It Works

1. **Start Quiz**: Answer whether a message is a "Scam" or "Real".
2. **Feedback**: See immediate explanations after each answer.
3. **Custom Checker**: Enter any suspicious message to test it.
4. **Scoring Engine**: Keywords from MySQL drive the logic.

---

## Run Locally

```bash
git clone https://github.com/gurveer15/FraudAware.git
cd FraudAware
python -m venv venv
# Activate virtual environment:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
---

## Video Demo

https://www.youtube.com/watch?v=KV7UF0LT_Qs

---



