from bottle import Bottle, template, request, redirect
import os

treino_app = Bottle()

# Banco de dados em memória
treinos = []

# Caminho das views
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIEWS_DIR = os.path.join(BASE_DIR, "views")

# Listagem
@treino_app.get('/')
def listar():
    return template("list.tpl", lookup=[VIEWS_DIR], lista=treinos)

# Criar – formulário
@treino_app.get('/create')
def create_form():
    return template("form.tpl", lookup=[VIEWS_DIR], treino=None)

# Criar – salvar
@treino_app.post('/create')
def create_save():
    nome = request.forms.get("nome")
    repeticoes = request.forms.get("repeticoes")
    tempo = request.forms.get("tempo")

    treinos.append({
        "nome": nome,
        "repeticoes": repeticoes,
        "tempo": tempo
    })

    redirect('/treinos')

# Editar – formulário
@treino_app.get('/edit/<id:int>')
def edit_form(id):
    if id < 0 or id >= len(treinos):
        return "Treino não encontrado."
    return template("form.tpl", lookup=[VIEWS_DIR], treino=treinos[id], id=id)

# Editar – salvar
@treino_app.post('/edit/<id:int>')
def edit_save(id):
    treinos[id]["nome"] = request.forms.get("nome")
    treinos[id]["repeticoes"] = request.forms.get("repeticoes")
    treinos[id]["tempo"] = request.forms.get("tempo")
    redirect('/treinos')

# Excluir
@treino_app.get('/delete/<id:int>')
def delete(id):
    if id < 0 or id >= len(treinos):
        return "Treino não encontrado."
    treinos.pop(id)
    redirect('/treinos')

