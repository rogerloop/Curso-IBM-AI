from flask import Flask, render_template, Response
import matplotlib

matplotlib.use('Agg')  # Utiliza un backend no interactivo
import matplotlib.pyplot as plt
import io

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/grafico.png')
def grafico():
    # Datos ficticios de inflación
    data = {
        "Año": list(range(2004, 2024)),
        "España": [3.0, 3.4, 3.5, 2.8, 4.1, -0.3, 1.8, 3.1, 2.4, 1.4, -0.2, -0.6, -0.2, 1.6, 1.7, 0.7, -0.3, 3.1, 8.3,
                   5.2],
        "Francia": [2.3, 2.8, 2.6, 1.8, 3.2, 0.1, 1.7, 2.3, 1.9, 0.9, 0.1, 0.0, 0.2, 1.2, 1.3, 0.9, -0.1, 2.8, 6.5,
                    4.0],
        "Alemania": [1.8, 1.9, 2.0, 2.2, 2.8, 0.2, 1.5, 2.1, 1.6, 1.0, 0.3, 0.4, 0.5, 1.5, 1.8, 1.4, 0.2, 3.0, 7.8,
                     4.5],
        "Italia": [2.5, 2.7, 2.9, 1.9, 3.7, 0.3, 1.6, 2.4, 2.0, 1.1, 0.5, 0.2, 0.3, 1.3, 1.6, 1.1, 0.0, 2.9, 6.8, 4.2],
    }

    # Crear el gráfico
    plt.figure(figsize=(12, 7))
    plt.plot(data["Año"], data["España"], marker='o', linestyle='-', color='blue', label='España')
    plt.plot(data["Año"], data["Francia"], marker='o', linestyle='-', color='green', label='Francia')
    plt.plot(data["Año"], data["Alemania"], marker='o', linestyle='-', color='red', label='Alemania')
    plt.plot(data["Año"], data["Italia"], marker='o', linestyle='-', color='purple', label='Italia')

    plt.title('Inflación Media (Últimos 20 años)')
    plt.xlabel('Año')
    plt.ylabel('Inflación (%)')
    plt.legend()
    plt.grid(True)

    # Guardar el gráfico en un objeto de bytes
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return Response(img.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
