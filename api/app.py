from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/comerciantes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'
db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Produto(db.Model):
    __tablename__ = 'cadastro_produtos'
    _id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    preco_normal = db.Column(db.Float, nullable=False)
    preco_promocional = db.Column(db.Float, nullable=False)
    comercio = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    validade_promocao = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            flash('Login bem-sucedido! Bem-vindo, {}!'.format(user.nome))
            return redirect(url_for('comerciantes'))
        else:
            flash('Usuário ou senha incorretos!')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/comerciantes')
def comerciantes():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('comerciantes.html', imagem_fundo='VenBarato.jpg')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        username = request.form['username']
        password = request.form['password']

        # Verificar se o nome de usuário já existe
        usuario_existente = Usuario.query.filter_by(username=username).first()
        if usuario_existente:
            flash('Nome de usuário já existe! Tente outro.')
            return redirect(url_for('cadastro'))

        novo_usuario = Usuario(nome=nome, username=username, password=password)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Usuário cadastrado com sucesso! Faça login para continuar.')
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/recebe_dados', methods=['POST'])
def recebe_dados():
    produto = request.form['produto']
    descricao = request.form['descricao']
    preco_normal = request.form['preco_normal']
    preco_promocional = request.form['preco_promocional']
    comercio = request.form['comercio']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    validade_promocao = request.form['validade_promocao']

    novo_produto = Produto(produto=produto, descricao=descricao, preco_normal=preco_normal, preco_promocional=preco_promocional, comercio=comercio, endereco=endereco, telefone=telefone, validade_promocao=validade_promocao)
    db.session.add(novo_produto)
    db.session.commit()

    return redirect(url_for('comerciantes'))

@app.route("/cadastro")
def cadastrar():
    return render_template("produtos.html")


@app.route('/produtos')
def lista_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)

@app.route('/pesquisar_clientes', methods=['GET'])
def pesquisar_clientes():
    query = request.args.get('query')
    if query:
        # Realizar a pesquisa no banco de dados
        resultados = Produto.query.filter(
            (Produto.produto.like(f'%{query}%')) |
            (Produto.descricao.like(f'%{query}%')) |
            (Produto.preco_normal.like(f'%{query}%')) |
            (Produto.preco_promocional.like(f'%{query}%')) |
            (Produto.comercio.like(f'%{query}%')) |
            (Produto.endereco.like(f'%{query}%')) |
            (Produto.telefone.like(f'%{query}%')) |
            (Produto.validade_promocao.like(f'%{query}%'))
        ).all()
    else:
        resultados = []

    return render_template('clientes.html', produtos=resultados)

@app.route('/consumidores')
def clientes():
    return render_template('clientes.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

app.config['HOST'] = 'localhost'
app.config['PORT'] = 4000
app.config['DEBUG'] = True

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
