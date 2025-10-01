from flask import Flask, request, jsonify

app = Flask(__name__)

# Sadə yaddaşda todo list
todos = []

@app.route('/')
def home():
    return "🚀 Flask Todo API-ya xoş gəldiniz! Endpoints: /todos"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    if not data or "task" not in data:
        return jsonify({"error": "Task daxil edilməyib"}), 400
    todo = {"id": len(todos) + 1, "task": data["task"]}
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": f"Task {todo_id} silindi!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
