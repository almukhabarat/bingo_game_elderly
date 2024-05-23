from flask import Flask

app = Flask(__name__)

# Endpoint to start the motor
@app.route('/give_candy', methods=['GET'])
def bingo_verified():
    # plaats hier if else statement logica voor het ontvangen van NAO6 bingo verificatie
    
    # Add your code here to start the motor
    # For now, let's just return a success message
    return 'geef_snoep'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
