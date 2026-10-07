# Calculadora de Salário Líquido

Este projeto foi uma atividade desenvolvida para meu curso de Análise e Desenvolvimento de Sistemas, no módulo sobre Frameworks para Desenvolvimento de Softwares. Nessa atividade, foram propostas algumas regras para o cálculo do salário líquido de uma pessoa com base no valor bruto e na quantidade de dependentes que ela possui.

## Sobre o projeto

No projeto foram definidas regras para o cálculo do INSS, do Imposto de Renda (IR) e um acréscimo de R$ 200,00 para cada dependente informado.

A regra do INSS determina que 8% do salário bruto seja descontado. Já para o IR, caso o salário bruto seja maior que R$ 2.500,00, é descontado 15% do salário bruto.

Também foram aplicados tratamentos para possíveis erros na entrada de dados, com validações realizadas no backend antes que o cálculo seja efetuado.

## Funcionalidades

* Calcular o salário líquido a partir do salário bruto e da quantidade de dependentes;
* Validar os dados informados pelo usuário;
* Exibir mensagens para entradas inválidas;
* Apresentar o resultado do cálculo em uma interface web.

## Tecnologias utilizadas

* Python
* Flask
* Jinja2
* HTML

## Como executar

1. Clone o repositório
git clone URL_DO_REPOSITORIO
2. Acesse a pasta do projeto
cd nome-do-projeto
3. Crie um ambiente virtual

Windows:

python -m venv venv

4. Ative o ambiente virtual

Windows PowerShell:

venv\Scripts\Activate.ps1

5. Instale o Flask
   
pip install flask

6. Execute a aplicação
   
python app.py

Após iniciar a aplicação, acesse o endereço exibido pelo Flask no navegador.

## Estrutura do projeto

Estrutura do projeto
arquivos/

├── templates/

│   └── index.html

├── app.py

├── calculo.py

├── validacoes.py

└── README.md


Principais arquivos

app.py

Responsável por inicializar a aplicação Flask, receber os dados enviados pelo formulário, chamar as funções de validação e cálculo e enviar as informações para a página HTML.

validacoes.py

Responsável pela conversão e validação dos valores recebidos pelo formulário, verificando se o salário e a quantidade de dependentes são válidos.

calculo.py

Contém a função responsável pelo cálculo do salário líquido de acordo com as regras definidas no projeto.

templates/index.html

Contém a interface da aplicação, incluindo o formulário para entrada dos dados e a exibição do resultado ou das mensagens de validação.

## Regras de cálculo

O cálculo utilizado pela aplicação segue as seguintes regras:

INSS: 8% do salário bruto.
Imposto de renda: 15% do salário bruto quando o salário bruto for superior a R$ 2.500,00.
Dependentes: R$ 200,00 adicionados ao salário líquido para cada dependente.

A fórmula utilizada é:

Salário Líquido = Salário Bruto - INSS - Imposto de Renda + Valor dos Dependentes

## Aprendizados

Este foi meu primeiro projeto utilizando o framework Flask para integrar as funcionalidades do Python ao navegador. Foi uma grande jornada, na qual aprendi sobre o Flask a cada passo que ia construindo e travando nos novos conceitos apresentados.

Durante o desenvolvimento, também pratiquei conceitos como criação de rotas, recebimento de dados através de formulários, validação de entradas e separação da lógica de validação e cálculo em diferentes arquivos.

O intuito deste projeto inicialmente não era colocá-lo no meu GitHub, porém me afeiçoei ao projeto ao longo do desenvolvimento e quis compartilhar essa pequena jornada e um pouco do que aprendi com ele.
