from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'helloworld!!!!' \
           'z'


if __name__ == "__main__":
    applicationon = app.run()
