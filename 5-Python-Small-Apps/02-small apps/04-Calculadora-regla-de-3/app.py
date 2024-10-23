from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])

        # Regla de tres simple: a/b = c/x, entonces x = (b*c)/a
        x = (b * c) / a
        return jsonify({"resultado": round(x, 2)})
    except ValueError:
        return jsonify({"error": "Por favor, ingrese números válidos."}), 400
    except ZeroDivisionError:
        return jsonify({"error": "No se puede dividir por cero."}), 400


if __name__ == '__main__':
    app.run(debug=True)
