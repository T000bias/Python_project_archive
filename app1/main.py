from flask import Flask

app = Flask(__name__)

@app.route('/') # Index page
def index():
    return 'Index page'

@app.route('/about-me') # About me page
def about():
    return "About me page"

if __name__ == '__main__':
    app.run()