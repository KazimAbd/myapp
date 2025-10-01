from flask import Flask
import random

app = Flask(__name__)

messages = [
    "Salam DevOps 👋",
    "Yeni versiya gəldi 🚀",
    "Docker + Kubernetes = ❤️",
    "CI/CD işlədi 🔥",
]

@app.route('/')
def hello():
    return random.choice(messages)

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/about')
def about():
    return "Bu mənim Flask ilə yazılmış demo tətbiqimdir 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
