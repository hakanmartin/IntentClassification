from flask import Flask, render_template, request
#from niyettespiti4 import process_user_input
from SVM import process_user_input_svm

app = Flask(__name__)

# Örnek bir chat geçmişi
chat_history = []


@app.route('/')
def index():
    return render_template('index.html', chat_history=chat_history)


@app.route('/process_text', methods=['POST'])
def process_text():
    user_input = request.form['user_input']
    #final_intent = process_user_input(user_input)  # Niyettespiti4 için
    final_intent = process_user_input_svm(user_input)  # SVM için

    chat_history.append((user_input, final_intent))

    return render_template('index.html', chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True)