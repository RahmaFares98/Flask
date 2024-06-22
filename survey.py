from flask import Flask, render_template, request #import what we need 

app = Flask(__name__)

@app.route('/')# round defult bage survey html 
def index():
    return render_template('survey.html')

@app.route('/result', methods=['POST']) # after post form will round Result html 
def result():
    form_data = request.form
    print(form_data)
    return render_template('result.html', data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
