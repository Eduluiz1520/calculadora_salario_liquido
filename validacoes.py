
# Validações

# conversão de valores

def converter_valores(salario_bruto, dependentes):
    

    erro = False;

    try:
        salario_bruto = float(salario_bruto);
        dependentes = float(dependentes);

    except ValueError:

        erro = True;

    if erro:
        return None;

    return salario_bruto, dependentes;



# Validação dos valores convertidos
def validar_valores(salario_bruto, dependentes):

    mensagem = "";

    valores = converter_valores(salario_bruto, dependentes);

    if valores is not None:

        salario_bruto, dependentes = valores

        if (salario_bruto < 0):
            print("Por favor digite um salário válido.");
            mensagem = "Por favor digite um salário válido.";
            
            return mensagem, None;
        
        elif (dependentes < 0 or dependentes %1 !=0):
            print("Por favor digite um número de dependentes válido.")
            mensagem = "Por favor digite um número de dependentes válido.";
            return mensagem, None;

        return mensagem, valores;
    else:
        
        print("Não são permitidos letras, somente numerais, seu bobo!");
        mensagem = "Não são permitidas letras, somente numerais, seu bobo!";
        return mensagem, None;




