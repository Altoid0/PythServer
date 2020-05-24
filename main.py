from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome_page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)