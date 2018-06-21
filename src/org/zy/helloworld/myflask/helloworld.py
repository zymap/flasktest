from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'helloworld!'

from flask import app as application
#
# from myflask import
#
# if __name__ == "__main__":
#     app.run()
