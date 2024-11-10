from flask import Flask, jsonify, send_file
import json

app = Flask(__name__)

@app.route('/get_obj', methods=['GET'])
def get_obj():
    return send_file('cube.obj', mimetype='application/octet-stream')

@app.route('/get_json', methods=['GET'])
def get_json():
    # Leer el contenido del archivo J.json
    with open('J.json', 'r') as json_file:
        data = json.load(json_file)  # Cargar el JSON desde el archivo

    return jsonify(data)  # Devolver el contenido como JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
