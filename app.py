import random

messages = [
    "Salam DevOps 👋",
    "Yeni versiya gəldi 🚀",
    "Docker + Kubernetes = ❤️",
    "CI/CD işlədi 🔥",
]

@app.route('/')
def hello():
    return random.choice(messages)
