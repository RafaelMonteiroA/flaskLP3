from flask import Flask , render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ
listaCPF = []
listaCNPJ = []

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

@app.route("/cpfValido", methods=["GET"])
def cpfValido():
    return render_template("cpfValido.html", cpf = listaCPF)

@app.route("/cnpjValido")
def cnpjValido():
    return render_template("cnpjValido.html", cnpj = listaCNPJ)

@app.route("/validarCPF")
def validarCPF():
    return render_template("validarCPF.html")

@app.route("/validarCNPJ")
def validarCNPJ():
    return render_template("validarCNPJ.html")

@app.route("/validarCPF", methods=["POST"])
def confirmandoCPF():
    if request.method == "POST":
        cpf = CPF()
        cpfNome = request.form["cpf"]
        cpf.validate(cpfNome)
    if cpf.validate(cpfNome) == False:
        return "CPF Inválido"
    else:
        listaCPF.append(cpfNome)
        return redirect(url_for("cpfValido"))

@app.route("/validarCNPJ", methods=["POST"])
def confirmandoCNPJ():
    if request.method == "POST":
        cnpj = CNPJ()
        cnpjNome = request.form["cnpj"]
        cnpj.validate(cnpjNome)
        if cnpj.validate(cnpjNome) == False:
            return "CNPJ Inválido"
        else:
            listaCNPJ.append(cnpjNome)
            return redirect(url_for("cnpjValido"))