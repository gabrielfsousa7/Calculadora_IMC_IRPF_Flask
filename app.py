"""Descricao: Aplicativo básico com duas rotas para calcular o IMC e o Calculo do imposto de renda de uma pessoa usando argumentos de URL e URLs Elegantes.
nome_arquivo: app.py 
nome_exercicio: Introdução ao Flask - Calculadora de IMC e IRPF usando argumentos de URL e URLs elegantes
nome_aluno: Gabriel Antônio Ferreira de Sousa
"""

from flask import Flask, request
app = Flask(__name__)

# Calculadora IMC

# Argumentos de URL
@app.route("/calculadora_imc")
def calculadora_imc_query():
    nome: str = request.args.get("nome")
    peso: float = float(request.args.get("peso"))
    altura: float = float(request.args.get("altura"))

    imc: float = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade" 

    return f"Olá {nome}, seu IMC é {imc:.2f} ({classificacao})"

#URLs elegantes
@app.route("/calculadora_imc/<nome>/<float:peso>/<float:altura>")
def calculadora_imc_elegante(nome: str, peso: float, altura: float):
    imc: float = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return f"Olá {nome}, seu IMC é {imc:.2f} ({classificacao})"


#Calculadora Imposto de Renda 

# Argumentos de URL
@app.route("/calculadora_irpf")
def calculadora_irpf_query():
    nome: str = request.args.get("nome")
    salario: float = float(request.args.get("salario"))

    if salario <= 2428.80:
        imposto = 0
        aliquota = "0% (isento)"
    elif salario <= 3751.48:
        imposto = salario * 0.075
        aliquota = "7,5%"
    elif salario <= 4664.68:
        imposto = salario * 0.15
        aliquota = "15%"
    elif salario <= 8049.00:
        imposto = salario * 0.225
        aliquota = "22,5%"
    else:
        imposto = salario * 0.275
        aliquota = "27,5%"

    salario_liquido: float = salario - imposto

    return f"Olá {nome}, salário: R$ {salario:.2f} | Imposto de Renda Pessoa Física (IRPF) ({aliquota}): R$ {imposto:.2f} | Líquido: R$ {salario_liquido:.2f}"

# URLs elegantes
@app.route("/calculadora_irpf/<nome>/<float:salario>")
def calculadora_irpf_elegante(nome: str, salario: float):
    if salario <= 2428.80:
        imposto = 0
        aliquota = "0% (isento)"
    elif salario <= 3751.48:
        imposto = salario * 0.075
        aliquota = "7,5%"
    elif salario <= 4664.68:
        imposto = salario * 0.15
        aliquota = "15%"
    elif salario <= 8049.00:
        imposto = salario * 0.225
        aliquota = "22,5%"
    else:
        imposto = salario * 0.275
        aliquota = "27,5%"

    salario_liquido: float = salario - imposto

    return f"Olá {nome}, salário: R$ {salario:.2f} | IRPF ({aliquota}): R$ {imposto:.2f} | Líquido: R$ {salario_liquido:.2f}"

# Tela inicial (homepage)
@app.route("/")
def inicio():
    return """
    <h1 style="
    text-align: center;
    color: #2c3e50;
    font-family: Arial, sans-serif;
    font-size: 32px;
    margin-top: 40px">Aplicação de calculadoras</h1>
    <p style="text-align: center;
    color: #555;
    font-family: Arial, sans-serif;
    font-size: 18px;
    margin-bottom: 25px;">Use uma das opções:</p>
    <ul style="list-style: none;
    padding: 0;
    margin: 0 auto;
    width: 320px;
    text-align: center;
    font-family: Arial, sans-serif;">
        <li style="text-align: center;">
            <a href="/calculadora_imc?nome=Pindorama&peso=120&altura=1.75">Calculadora de Índice de Massa Corporal (IMC)</a>
        </li>
        <li style="text-align: center;">
            <a href="/calculadora_irpf?nome=Clodosvaldo&salario=5200">Calculadora de Imposto de Renda Pessoa Física (IRPF)</a>
        </li>
    </ul>
    <br />
    <footer style="
    text-align: center;
    color: #777;
    line-height: 1.6;
    border-top: 1px solid #ddd;"><br />Introdução ao Flask<br />Gabriel Antônio Ferreira de Sousa<br />2° Termo Desenvolvimento de Software Multiplataforma - Fatec Olímpia 
    """

if __name__ == "__main__":
    app.run(debug=True)