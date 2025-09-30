from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Salam! Bu, CI/CD test application v1.0.1  🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
