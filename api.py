from flask import Flask, jsonify
app = Flask(__name__)

def calcular_fatorial(num):
    if num == 0:
        return 1
    else:
        return num * calcular_fatorial(num-1)
@app.route('/fatorial/<int:num>')

def fatorial(num):
    resultado = calcular_fatorial(num)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
