from flask import Flask, render_template, request
import re
email_text = request.form['email_text']

app = Flask(__name__)

def detect_spam(email_text):
    spam_patterns = [
        "buy now",
        "earn money",
        "work from home",
        "cash prize",
        "click here",
        "get rich quick",
        "double your",
        "free gift",
        "no obligation",
        "money back",
        "discount",
        "guarantee",
        "debt",
        "Double your",
        "lowest price",
        "lowest rates",
        "lottery",
        "winner",
        "prize",
        "spam",
        "unsubscribe",
        "opt-out",
        "mortgage",
        "refinance",
        "consolidate",
        "extra income",
        "make money",
        "miracle",
        "obligation",
        "promise",
        "social security number",
        "stop snoring",
        "viagra",
        "weight loss"
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, email_text, re.IGNORECASE):
            return "It's a spam email !"
    
    return "It's not spam email !"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    email_text = request.form['email_text']
    result = detect_spam(email_text)
    return render_template('result.html', email_text=email_text, result=result)

if __name__ == '__main__':
    app.run(debug=True)
