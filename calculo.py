# Cálculo



def calcular_salario(salario_bruto, dependentes):

    if (salario_bruto > 2500):
        imposto_renda = salario_bruto * 0.15;
    else:
        imposto_renda = 0;
    
    inss = salario_bruto * 0.08;    
    dependetes_valor = dependentes * 200;
    salario_liquido = salario_bruto - inss - imposto_renda + dependetes_valor;

    print(salario_liquido);
    return salario_liquido;

# valores = converter_valores(salario_bruto, dependentes);


# if validar_valores(salario_bruto, dependentes):
#     calcular_salario(salario_bruto, dependentes);