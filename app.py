from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, GitHub Actions!"

@app.route('/status')
def status():
    return "App is running fine!"

if __name__ == '__main__':
    app.run(debug=True)