from bottle import Bottle, run, static_file
from app.controllers.treino_controller import treino_app
import os

app = Bottle()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIEWS_DIR = os.path.join(BASE_DIR, "app", "views")
STATIC_DIR = os.path.join(BASE_DIR, "app", "static")

print("[DEBUG] VIEWS_DIR =", VIEWS_DIR)
print("[DEBUG] STATIC_DIR =", STATIC_DIR)

# Rotas estáticas
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root=STATIC_DIR)

# Registra o app de treinos
app.mount('/treinos', treino_app)

run(app, host='localhost', port=8080, debug=True, reloader=True)
