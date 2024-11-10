from flask import Flask, send_file, jsonify

app = Flask(__name__)

# Ruta para obtener el archivo .obj
@app.route('/get_obj', methods=['GET'])
def get_obj():
    try:
        return send_file('cube.obj', mimetype='application/octet-stream', as_attachment=True)
    except Exception as e:
        return str(e), 500

# Ruta para obtener el archivo .json
@app.route('/get_json', methods=['GET'])
def get_json():
    try:
        with open('J.json', 'r') as json_file:
            data = json_file.read()
        return jsonify(data)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
