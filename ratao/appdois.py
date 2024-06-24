from flask import Flask , render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

app = Flask(__name__)

@app.route("/geradorCPF")
def geradorCPF():
    cpf = CPF()
    novoCPF = cpf.generate(True)
    return render_template("geradorCPF.html", cpf = novoCPF)

@app.route("/geradorCNPJ")
def geradorCNPJ():
    cnpj = CNPJ()
    novoCNPJ = cnpj.generate(True)
    return render_template("geradorCNPJ.html", cnpj = novoCNPJ)

@app.route("/cpfValido")
def cpfValido():
    cpf = CPF()
    novoCPF = cpf.generate(True)
    return render_template("cpfValido.html", cpf = novoCPF)

@app.route("/cnpjValido")
def cnpjValido():
    cnpj = CNPJ()
    novoCNPJ = cnpj.generate(True)
    return render_template("cnpjValido.html", cnpj = novoCNPJ)

@app.route("/validarCPF")
def validarCPF():
    return render_template("validarCPF.html")

@app.route("/validarCNPJ")
def validarCNPJ():
    return render_template("validarCNPJ.html")

@app.route("/validarCPF", methods=["GET", "POST"])
def confirmandoCPF():
    if request.method == "POST":
        cpf = CPF()
        cpfNome = request.form["cpf"]
        cpf.validate(cpfNome)
    return redirect(url_for("cpfValido"))

@app.route("/validarCNPJ", methods=["GET", "POST"])
def confirmandoCNPJ():
    if request.method == "POST":
        cnpj = CNPJ()
        cnpjNome = request.form["cnpj"]
        cnpj.validate(cnpjNome)
    return redirect(url_for("cnpjValido"))