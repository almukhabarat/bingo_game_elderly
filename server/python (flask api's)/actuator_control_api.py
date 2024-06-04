from flask import Flask, request, jsonify
from queue import Queue
from threading import Lock
import time

app = Flask(__name__)

# Create a thread-safe queue and a lock for the latest command
command_queue = Queue()
command_lock = Lock()

@app.route('/set_command', methods=['POST'])
def set_command():
    global latest_command
    command = request.json.get('command')
    if command:
        with command_lock:
            command_queue.put(command)
        return 'Command set successfully', 200
    else:
        return 'No command provided', 400

@app.route('/get_command', methods=['GET'])
def get_command():
    global latest_command
    start_time = time.time()
    timeout = 30  # Timeout after 30 seconds
    
    while time.time() - start_time <= timeout:
        with command_lock:
            if not command_queue.empty():
                command = command_queue.get()
                return jsonify({'command': command})
        time.sleep(0.1)  # Sleep briefly to avoid a busy wait
    
    return jsonify({'command': command})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# curl -X POST -H "Content-Type: application/json" -d '{"command": "geef snoepje ah zahbi"}' http://145.92.8.134/api/set_command

# curl -X POST -H "Content-Type: application/json" -d '{"command": "Draaien pls"}' http://145.92.8.134/api/set_command

# curl -X POST -H "Content-Type: application/json" -d '{"command": "loslaten pls"}' http://145.92.8.134/api/set_command

#####################################################

