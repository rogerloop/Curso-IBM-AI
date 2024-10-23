from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        dni = request.form['dni']
        localidad = request.form['localidad']

        # Crear el PDF
        pdf = FPDF()
        pdf.add_page()

        # Agregar contenido al PDF
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informacion de la Persona", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True)
        pdf.cell(200, 10, txt=f"Apellido: {apellido}", ln=True)
        pdf.cell(200, 10, txt=f"Edad: {edad}", ln=True)
        pdf.cell(200, 10, txt=f"DNI: {dni}", ln=True)
        pdf.cell(200, 10, txt=f"Localidad: {localidad}", ln=True)

        # Guardar el PDF en un archivo temporal
        pdf_filename = f"{nombre}_{apellido}.pdf"
        pdf.output(pdf_filename)

        # Enviar el archivo PDF al cliente
        return send_file(pdf_filename, as_attachment=True)

    return render_template('form.html')

# Ejecutar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
