from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    ]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  # Append request_body directly
    return jsonify({"label": 25 , "done": False})

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)