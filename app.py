from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world, welcome to this demo of CD"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
