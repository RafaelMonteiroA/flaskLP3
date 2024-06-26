from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home(): 
    return '<h1>Home</h1>'

@app.route("/contato")
def contato(): 
    return '<h1>Contato</h1>'

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = obter_produto())
 
@app.route("/produtos/<nome>")
def produto(nome):
    for produto in produtos.lista_produtos:
        if produto["nome"] == nome:
            return render_template("produto.html", produto=produto)


    return "Produto não existe!" 

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos", methods=["POST"])
def obter_produto():
   with open("produtos.csv", 'r') as file:
    lista_produtos = []
    for linha in file:
        nome, descricao, preco, imagem = linha.split(",")
        produto = {
            "nome": nome,
            "descricao": descricao,
            "preco": float(preco),
            "imagem": imagem
        }
        lista_produtos.append(produto)
    return redirect(url_for("home"))

def salvar_produto(p):
    linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
    with open(produtos.csv, 'a') as file:
        file.write(linha)

app.run(port=5001)