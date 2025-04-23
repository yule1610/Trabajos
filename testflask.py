from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tareas iniciales
data = [
    "tareas:", "Estudiar matemáticas", "Hacer ejercicio", "Leer un libro"
]

# Ruta para obtener todas las tareas
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Ruta para agregar una nueva tarea
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()  # Esto obtiene los datos JSON del cuerpo de la solicitud

    if new_item and 'tarea' in new_item:
        data.append(new_item['tarea'])
        return jsonify({
            'message': 'Tarea agregada exitosamente.',
            'data': data
        }), 201
    else:
        return jsonify({'error': 'El formato debe incluir el campo "tarea".'}), 400

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
