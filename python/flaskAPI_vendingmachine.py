from flask import Flask

app = Flask(__name__)

# Endpoint to start the motor
@app.route('/start_motor', methods=['GET'])
def start_motor():
    # Add your code here to start the motor
    # For now, let's just return a success message
    return 'Motor started!'

# Endpoint to stop the motor
@app.route('/stop_motor', methods=['GET'])
def stop_motor():
    # Add your code here to stop the motor
    # For now, let's just return a success message
    return 'Motor stopped!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
