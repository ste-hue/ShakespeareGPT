from flask import Flask, request, render_template, session
from flask_session import Session
import openai
import os
from dotenv import load_dotenv

load_dotenv()


from shakespeareGPT import generate_shakespeare_text

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    session.clear()  # Clear the session when visiting the home page
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    user_prompt = request.form['prompt']
    session['history'] = session.get('history', '') + f' You: {user_prompt}\n'
    generated_text = generate_shakespeare_text(session['history'])
    session['history'] += f'Shakespeare: {generated_text}\n'
    return render_template('response.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
