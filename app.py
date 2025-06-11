from flask import Flask, render_template, request
from grader import grade_essay

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    if request.method == 'POST':
        essay = request.form['essay']
        score = grade_essay(essay)
    return render_template('index.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
