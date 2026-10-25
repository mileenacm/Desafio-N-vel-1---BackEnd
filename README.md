
O objetivo do Sistema de Ponto de Venda (PDV) é calcular descontos em compras de forma automática e progressiva. O programa atua como um caixa de loja, processando múltiplas vendas em sequência e gerando um relatório financeiro completo ao fim do expediente, detalhando o faturamento bruto, o total de descontos concedidos e a receita líquida final.

----

Como funciona:

O sistema começa criando uma lista vazia chamada historico_compras. Em seguida, entra em um loop infinito controlado pela variável maquina, exibindo um menu com 3 opções controladas por uma estrutura match/case.

Registro de Vendas (Opção 1)
Ao escolher a opção 1, o sistema entra em um segundo loop (de compra) para que o operador possa registrar várias compras seguidas sem precisar voltar ao menu inicial.

Entrada e Validação: O usuário digita a idade e o valor. Se digitar 0, o loop de compras é encerrado. Se digitar valores negativos, o "continue" ignora a tentativa e reinicia o loop.

Cálculo de Descontos: A variável valor_novo recebe o valor original e passa por condições.
Se a idade for ≥ 65, aplica-se 20% de desconto. Se, após esse desconto, o valor ainda for > 100, aplica-se mais 10%.
Por outro lado, se a idade for < 65 mas o valor for > 100, aplica-se 10%.

Os dados de cada compra válida são adicionados à lista historico_compras no formato de um dicionário, guardando tanto o valor bruto quanto o valor final cobrado.

Consulta de Regras (Opção 2)
Detalha as regras matemáticas do desconto progressivo e pergunta se o usuário deseja voltar ao menu ou desligar o sistema.

Resumo e Encerramento (Opção 3)
Quando o usuário decide sair, a variável maquina se torna False, preparando o programa para desligar. Antes de fechar, o sistema exibe os dados salvos:

Usa len(historico_compras) para descobrir quantas compras foram feitas.
Tem a função sum() combinada com laços internos (list comprehensions) para somar todos os valores da chave "bruto" e todos os valores da chave "final".
Imprime na tela um relatório com a quantidade de clientes atendidos, o total vendido sem descontos, o valor total que a loja deixou de cobrar (descontos concedidos) e o total em dinheiro que efetivamente entrou no caixa.

----

Como executar o código:
É necessário ter Python instalado na sua máquina (versão 3.10 ou superior recomendada devido ao uso do match/case).
Salve o código em um arquivo chamado pdv.py, abra o terminal na mesma pasta do arquivo e execute o comando python pdv.py

----
Tabela de exemplos:

| #  | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|:--:|:----------:|:-----:|:--------------:|:--------------:|:--------------------:|
| 1  | 50.00      | 30    | 0%             | 0%             | R$ 50.00             |
| 2  | 100.00     | 30    | 0%             | 0%             | R$ 100.00            |
| 3  | 80.00      | 65    | 20%            | 0%             | R$ 64.00             |
| 4  | 100.00     | 70    | 20%            | 0%             | R$ 80.00             |
| 5  | 125.00     | 70    | 20%            | 0%             | R$ 100.00            |
| 6  | 200.00     | 30    | 0%             | 10%            | R$ 180.00            |
| 7  | 101.00     | 30    | 0%             | 10%            | R$ 90.90             |
| 8  | 200.00     | 65    | 20%            | 10%            | R$ 144.00            |
| 9  | 1000.00    | 80    | 20%            | 10%            | R$ 720.00            |
| 10 | 200.00     | 64    | 0%             | 10%            | R$ 180.00            |
 
