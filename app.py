from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed to use sessions


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sift@7799",
        database="FraudAware"
    )


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    if 'score' not in session:
        session['score'] = 0
        session['question_number'] = 0

        # Fetch 5 random questions from database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT message, correct_answer, explanation
            FROM quiz_questions
            WHERE message IS NOT NULL AND correct_answer IS NOT NULL AND explanation IS NOT NULL
            ORDER BY RAND()
            LIMIT 5
        """)
        
        quiz_data = cursor.fetchall()
        conn.close()

        # Print and filter quiz_data to make sure each row has 3 values
        filtered_data = []
        for i, row in enumerate(quiz_data):
            print(f"Row {i}: {row} (Length: {len(row)})")
            if len(row) == 3:
                filtered_data.append(row)

        session['questions'] = filtered_data

        if not session['questions']:
            return "<h3>Error: No valid quiz questions found. Please check your database.</h3>"

    if request.method == 'POST':
        user_answer = request.form['user_answer']
        correct_answer = request.form['correct_answer']
        explanation = request.form['explanation']

        feedback = {
            'correct': user_answer == correct_answer,
            'explanation': explanation,
            'user_answer': user_answer,
            'correct_answer': correct_answer
        }

        if feedback['correct']:
            session['score'] += 1

        session['last_feedback'] = feedback
        return redirect(url_for('feedback'))

    qn_number = session['question_number']
    if qn_number >= 5:
        final_score = session['score']
        session.clear()
        return f"<h2>Quiz Completed!</h2><p>Your score: {final_score} / 5</p><a href='/quiz'>Restart</a>"

    print("Question tuple:", session['questions'][qn_number])
    print("Length:", len(session['questions'][qn_number]))

    msg, ans, expl = session['questions'][qn_number]
    session['question_number'] += 1
    return render_template('quiz.html', message=msg, answer=ans, explanation=expl)


@app.route("/feedback")
def feedback():
    data = session.get('last_feedback', {})
    return render_template('feedback.html', feedback=data)


@app.route("/check", methods=['GET', 'POST'])
def check():
    result = ""
    message = ""

    if request.method == 'POST':
        message = request.form['message'].lower()
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT keyword, weight FROM scam_keywords")
        scam_keywords = cursor.fetchall()

        cursor.execute("SELECT keyword FROM safe_keywords")
        safe_keywords = [row[0] for row in cursor.fetchall()]

        score = 0
        matched_keywords = []

        for keyword, weight in scam_keywords:
            if keyword in message:
                score += weight
                matched_keywords.append(keyword)

        for keyword in safe_keywords:
            if keyword in message:
                score -= 1

        if score >= 3:
            result = f"⚠️ Likely SCAM (triggered keywords: {', '.join(matched_keywords)})"
        elif score == 2:
            result = f"⚠️ Suspicious — review carefully (keywords: {', '.join(matched_keywords)})"
        else:
            result = "✅ Looks safe, but always verify with official sources."

        cursor.close()
        conn.close()

    return render_template('check.html', result=result, message=message)

@app.route('/clear')
def clear():
    session.clear()
    return "Session cleared."

if __name__ == '__main__':
    app.run(debug=True)
