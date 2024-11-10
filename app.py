from flask import Flask, send_file, jsonify

app = Flask(__name__)

# Ruta para descargar el archivo .obj
@app.route('/model', methods=['GET'])
def download_model():
    return send_file('path/to/your/model.obj', as_attachment=True)

# Ruta para obtener los parámetros en formato .json
@app.route('/parameters', methods=['GET'])
def get_parameters():
    return jsonify({
        "machine_name": "Demo Machine",
        "parameters": {
            "temperature": 45.0,
            "pressure": 101.3,
            "speed": 1200
        },
        "units": {
            "temperature": "Celsius",
            "pressure": "kPa",
            "speed": "RPM"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
