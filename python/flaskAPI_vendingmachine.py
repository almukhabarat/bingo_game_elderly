from flask import Flask, request, jsonify

app = Flask(__name__)

# This variable will store the current command for the stepper motor
command = ""

@app.route('/control', methods=['GET'])
def control():
    global command
    return jsonify({"command": command})

@app.route('/set_command', methods=['POST'])
def set_command():
    global command
    data = request.get_json()
    if 'command' in data:
        command = data['command']
        return jsonify({"status": "success", "command": command})
    else:
        return jsonify({"status": "error", "message": "No command provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
