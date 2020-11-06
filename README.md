<h1>l-systems</h1>
<h2>Feito por Lucas Caffer - 081180024</h2>

<h2>Sobre</h2>
<p>Linguagem de programação utilizada: Python 3.9.0</p>
<p>Feito por Lucas Caffer - 081180024</p>

<h2>Modo de utilizar</h2>
<p>O programa deve ser executado pelo arquivo "l-systems.py", para a sua execução é necessário o arquivo "Regras.txt", que possuirá toda a gramática e regras que a aplicação aceitará.</p>
<p>O arquivo "Regras.txt" funcionará da seguinte maneira:</p>
<p>Será aceito como alfabeto, qualquer letra, além dos simbolos: "+", "-", "[", "]". Porém apenas a letra "F" faz com que sejá desenhada uma linha, o simbolo "+" faz com que sejá feita uma curva a esquerda, de acordo com o ângulo informado, o simbolo "-" faz com que sejá feita uma curva a direita, também de acordo com o ângulo, o simbolo "[", faz com que seja gravado a atual posição e o atual ângulo na memoria, e o simbolo "]" consome a ultima posição e ângulo gravados com o "[", e retorna para elas.</p>
<p>Na primeira linha deverá ser informada todas as variaveis, separadas por ",".</p>
<p>Na segunda linha deverá ser informada todas as constantes, separadas por ",".</p>
<p>Na terceira linha é informada a regra inicial.</p>
<p>Na quarta linha é informado um número, que corresponde as curvas feitas pelos simbolos "+" ,e "-".</p>
<p>Na quinta linha é informado um número, que corresponde ao angulo inicial.</p>
<p>Na sexta linha é informado um número inteiro, que corresponde ao número de execuções do programa.</p>
<p>Da setima linha em diante são informadas as regras de produção, que definem como as variáveis podem ser substituidas por constantes, ou outras variáveis. Elas deverão seguir o padrão: VARIÁVEL -> SEQUENCIA DE CARACTERES. Deverá haver apenas uma regra por linha, todas as demais linhas deverão contém regras de produção</p>