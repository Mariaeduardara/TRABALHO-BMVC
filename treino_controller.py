from bottle import Bottle, run, template, request, redirect

app = Bottle()

treinos = []  # banco de dados simples


@app.route('/')
def home():
    return "<h1>BMVC Funcionando!</h1><a href='/treinos'>Ir para Treinos</a>"


@app.route('/treinos')
def lista_treinos():
    return template("""
        <h1>Treinos</h1>
        <a href='/treinos/create'>Criar novo</a>
        <ul>
        % for i, t in enumerate(treinos):
            <li>{{t}} <a href='/treinos/delete/{{i}}'>Excluir</a></li>
        % end
        </ul>
    """, treinos=treinos)


@app.route('/treinos/create')
def form_create():
    return """
        <h1>Novo Treino</h1>
        <form action="/treinos/create" method="post">
            Nome: <input name="nome"><br>
            <button type="submit">Salvar</button>
        </form>
    """


@app.post('/treinos/create')
def create():
    nome = request.forms.get("nome")
    treinos.append(nome)
    return redirect("/treinos")


@app.get('/treinos/delete/<id:int>')
def delete(id):
    treinos.pop(id)
    return redirect("/treinos")


run(app, host='localhost', port=8080, reloader=True)
