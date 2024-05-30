from flask import Flask, request, jsonify
import time

app = Flask(__name__)

latest_command = None

@app.route('/set_command', methods=['POST'])
def set_command():
    global latest_command
    command = request.json.get('command')
    if command:
        latest_command = command
        return 'Command set successfully', 200
    else:
        return 'No command provided', 400

@app.route('/get_command', methods=['GET'])
def get_command():
    global latest_command
    start_time = time.time()
    timeout = 30  # Timeout after 30 seconds
    
    while latest_command is None:
        if time.time() - start_time > timeout:
            return jsonify({'command': ''})  # Return an empty command if timeout
        time.sleep(0.1)  # Sleep briefly to avoid a busy wait
    
    command = latest_command
    latest_command = None
    return jsonify({'command': command})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


# curl -X POST -H "Content-Type: application/json" -d '{"command": "geef snoepje ah zahbi"}' http://145.92.8.134/set_command

