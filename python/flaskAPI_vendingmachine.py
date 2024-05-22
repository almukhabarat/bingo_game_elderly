from flask import Flask, jsonify, request

app = Flask(__name__)

instructions = []

@app.route('/instructions', methods=['GET'])
def get_instructions():
    return jsonify(instructions)

@app.route('/instructions', methods=['POST'])
def add_instruction():
    instruction = request.json
    instructions.append(instruction)
    return jsonify({"message": "Instruction added successfully"})

# Example endpoint to trigger moving the motor
@app.route('/move_motor', methods=['POST'])
def move_motor():
    # Add "move_motor" instruction
    instructions.append({"instruction": "move_motor"})
    return jsonify({"message": "Move motor instruction added"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
