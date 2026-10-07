from flask import Flask, render_template, request;
from validacoes import validar_valores;
from calculo import calcular_salario;


app = Flask(__name__);

@app.route("/", methods=["GET", "POST"])
def inicio():

    mensagem = "";
    salario_liquido = None;

    if request.method == "POST":

        salario_bruto = request.form["salario_bruto"];
        dependentes = request.form["dependentes"];

        mensagem, valores = validar_valores(salario_bruto, dependentes);

        if valores is not None:

            salario_bruto, dependentes = valores;

            salario_liquido = calcular_salario(salario_bruto, dependentes);

        print(salario_bruto);
        print(dependentes);

    
    return render_template("index.html", mensagem=mensagem, salario_liquido=salario_liquido);

if __name__ == "__main__":
    app.run(debug=True);
