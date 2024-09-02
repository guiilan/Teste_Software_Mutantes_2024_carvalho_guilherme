Guilherme Ilan Barboza Carvalho

Atividade 2  – Testes de mutação

Repositório escolhido: https://github.com/harsilspatel/toy-robot-simulator

Meu repositório: https://github.com/guiilan/Teste_Software_Mutantes_2024_carvalho_guilherme

O projeto escolhido é o toy-robot-simulator, desenvolvido em Python 3, com cenários de teste definidos utilizando pytest. Para a realização dos testes de mutação, será utilizado o Mutmut, que é uma ferramenta projetada para detectar mutantes no código, garantindo a robustez dos testes existentes.

Este robô simulado opera em uma superfície 2D quadrada, onde pode ser posicionado em qualquer ponto dentro dos limites da mesa. Ele pode realizar movimentos simples, como:
Posicionar-se (place): Define a posição inicial do robô e sua direção (Norte, Sul, Leste, Oeste).
Mover-se (move): Avança uma unidade na direção em que está virado, se o movimento mantiver o robô dentro dos limites da mesa.
Girar à esquerda ou à direita (LEFT e RIGHT): Muda a direção do robô em 90 graus.
Reportar posição (report): Informa a posição atual do robô e a direção em que está virado.
O robô segue comandos recebidos, validando suas ações para garantir que não saia da superfície.
```
https://github.com/harsilspatel/toy-robot-simulator
```

Primeiro, executamos os testes existentes no projeto com o comando pytest -vv test.py para verificar a cobertura de código. Isso nos ajuda a identificar quais partes do código estão sendo adequadamente testadas e detectar eventuais lacunas. O objetivo é garantir que os testes atuais sejam robustos e completos antes de aplicar os testes de mutação. Dessa forma, podemos comparar os resultados antes e depois dos aprimoramentos feitos pelos testes de mutação, identificando possíveis melhorias na cobertura e eficácia dos testes.
```
(venv) PS C:\Users\guiil\atividade-teste\teste_atividade_2> pytest test.py
===================================================================================================================== test session starts ===================================================================================================================== 
platform win32 -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
rootdir: C:\Users\guiil\atividade-teste\teste_atividade_2
plugins: cov-5.0.0
collected 106 items                                                                                                                                                                                                                                             

test.py ..........................................................................................................                                                                                                                                       [100%]

===================================================================================================================== 106 passed in 5.06s =====================================================================================================================
```
Aqui, verificamos que todos os testes disponíveis estão funcionando corretamente. Para monitorar melhor a cobertura de código da aplicação, executamos o comando pytest -vv test.py --cov. 
```
---------- coverage: platform win32, python 3.11.9-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
RobotSimulator.py      67      0   100%
test.py                76      0   100%
---------------------------------------
TOTAL                 143      0   100%


===================================================================================================================== 106 passed in 8.64s =====================================================================================================================
```
Constatamos que 100% do código está sendo testado. Com isso, avançamos para os testes de mutação usando o Mutmut. Para isso, executamos o comando mutmut run após realizar a devida configuração no arquivo setup.cfg.
```
[mutmut]
tests_dir=C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
paths_to_mutate=C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
runner=python -m pytest test.py
```
Após rodar o comando mutmut run, acompanhamos no terminal o processo dos testes de mutação, onde podemos observar o total de mutantes gerados, quantos foram eliminados e quantos sobreviveram.

```
Legend for output:
🎉 Killed mutants.   The goal is for everything to end up in this bucket.
⏰ Timeout.          Test suite took 10 times as long as the baseline so were killed.
🤔 Suspicious.       Tests took a long time, but not long enough to be fatal.
🙁 Survived.         This means your tests need to be expanded.
🔇 Skipped.          Skipped.

mutmut cache is out of date, clearing it...
1. Running tests without mutations
⠏ Running...Done

2. Checking mutants
⠦ 119/119  🎉 90  ⏰ 0  🤔 0  🙁 29  🔇 0
```

Na saída, observamos que 29 dos 119 mutantes sobreviveram. Para obter detalhes sobre esses mutantes, usamos o comando mutmut html, que gera um arquivo .html com informações detalhadas dos testes de mutação realizados e as alterações feitas.

No arquivo gerado, podemos observar os mutantes, incluindo os mutantes 12, 13 e 14, que usaremos como exemplo para uma análise mais detalhada a seguir.
```
C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
Killed 90 out of 119 mutants
Survived
Survived mutation testing. These mutants show holes in your test suite.
Mutant 12
--- C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
+++ C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
@@ -29,7 +29,7 @@
 
 
 def generate_command(table_width, table_length):
-	command = random.choice(['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT'])
+	command = random.choice(['XXPLACEXX', 'MOVE', 'REPORT', 'LEFT', 'RIGHT'])
 	if command == 'PLACE':
 		x = random.randint(0, int(1.5 * table_width))
 		y = random.randint(0, int(1.5 * table_length))
Mutant 13
--- C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
+++ C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
@@ -29,7 +29,7 @@
 
 
 def generate_command(table_width, table_length):
-	command = random.choice(['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT'])
+	command = random.choice(['PLACE', 'XXMOVEXX', 'REPORT', 'LEFT', 'RIGHT'])
 	if command == 'PLACE':
 		x = random.randint(0, int(1.5 * table_width))
 		y = random.randint(0, int(1.5 * table_length))
Mutant 14
--- C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
+++ C:/Users/guiil/atividade-teste/teste_atividade_2/test.py
@@ -29,7 +29,7 @@
 
 
 def generate_command(table_width, table_length):
-	command = random.choice(['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT'])
+	command = random.choice(['PLACE', 'MOVE', 'XXREPORTXX', 'LEFT', 'RIGHT'])
 	if command == 'PLACE':
 		x = random.randint(0, int(1.5 * table_width))
 		y = random.randint(0, int(1.5 * table_length))
```       

``` 
def generate_command(table_width, table_length):
	command = random.choice(['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT'])
	if command == 'PLACE':
		x = random.randint(0, int(1.5 * table_width))
		y = random.randint(0, int(1.5 * table_length))
		dir = random.choice(list(Direction))
		command += ' {},{},{}'.format(x, y, dir.name)

	return command
``` 

Os mutantes são oriundos dessa função e sobrevivem porque as mudanças feitas nos comandos (PLACE, MOVE, REPORT) não são detectadas pelos testes existentes. Vamos analisar cada mutante em detalhes:

Mutante 12:
Mudança: O comando PLACE foi substituído por XXPLACEXX.
Motivo da sobrevivência: Os testes não validam se o comando gerado é exatamente PLACE. Assim, quando o mutante altera PLACE para XXPLACEXX, o teste não detecta a mudança porque ele não verifica o valor específico dos comandos gerados, ou o código que lida com o comando PLACE nunca é chamado nos testes.

Mutante 13:
Mudança: O comando MOVE foi substituído por XXMOVEXX.
Motivo da sobrevivência: De forma semelhante ao Mutante 12, os testes não verificam especificamente se MOVE é um dos comandos gerados, permitindo que o mutante sobreviva.

Mutante 14:
Mudança: O comando REPORT foi substituído por XXREPORTXX.
Motivo da sobrevivência: Como nos outros casos, a mudança do comando REPORT para XXREPORTXX não é detectada pelos testes. Isso indica que os testes não cobrem a verificação dos comandos gerados ou não exercitam suficientemente os cenários onde esses comandos são críticos.
A solução proposta envolve a introdução da função verifyArray para garantir que todos os comandos gerados sejam válidos antes de serem utilizados. Vou explicar como essa solução elimina os mutantes:

``` 
def generate_command(table_width, table_length):
	command = random.choice(verifyArray(['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT']))
	if command == 'PLACE':
		x = random.randint(0, int(1.5 * table_width))
		y = random.randint(0, int(1.5 * table_length))
		dir = random.choice(list(Direction))
		command += ' {},{},{}'.format(x, y, dir.name)

	return command

def verifyArray(ar):
    valid_commands = ['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT']
    if all(command in valid_commands for command in ar):
        return ar
    else:
        return []
``` 

A função verifyArray:Esta função recebe um array de comandos (ar) e verifica se todos os comandos nesse array pertencem a um conjunto de comandos válidos: 'PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT'.
Se todos os comandos forem válidos, o array é retornado como está. Se houver algum comando inválido, a função retorna um array vazio.
Modificação no generate_command:
No código original, o comando era selecionado aleatoriamente de uma lista fixa de comandos válidos. No código proposto, a lista de comandos válidos é passada pela função verifyArray.
Isso significa que, se o array passado para random.choice contiver algum comando inválido, a função verifyArray retornará um array vazio, e nenhum comando inválido será selecionado.
Para testarmos novamente executaremos novamente o “mutmut run”, e veremos os mutantes sobreviventes.

``` 
Legend for output:
🎉 Killed mutants.   The goal is for everything to end up in this bucket.
⏰ Timeout.          Test suite took 10 times as long as the baseline so were killed.
🤔 Suspicious.       Tests took a long time, but not long enough to be fatal.
🙁 Survived.         This means your tests need to be expanded.
🔇 Skipped.          Skipped.

mutmut cache is out of date, clearing it...
1. Running tests without mutations
⠏ Running...Done

2. Checking mutants
⠴ 126/126  🎉 102  ⏰ 0  🤔 0  🙁 24  🔇 0
``` 

Vemos que foram gerados 126 mutantes, mas o número de sobreviventes diminuiu para 24, indicando que mais mutantes foram eliminados. Agora, executaremos o comando mutmut html para detalhar os mutantes sobreviventes.


Na saída do arquivo HTML, observamos que os mutantes usados como exemplos (12, 13 e 14) não existem mais, graças à introdução da função verifyArray. Essa função cria uma barreira adicional que impede a geração e o uso de comandos inválidos, como os introduzidos pelos mutantes. Como resultado, os testes existentes agora conseguem detectar essas mutações, garantindo que os comandos gerados sejam sempre válidos e estejam em conformidade com o esperado.
O projeto "toy-robot-simulator" foi escolhido para demonstrar a aplicação de testes de mutação usando a ferramenta Mutmut. Após garantir que todos os testes existentes cobrem 100% do código, avançamos para os testes de mutação. Inicialmente, 29 dos 119 mutantes sobreviveram, evidenciando limitações nos testes. A introdução da função verifyArray foi essencial para eliminar mutantes relacionados a comandos inválidos. Após a aplicação dessa solução, o número de mutantes sobreviventes reduziu para 24, confirmando a eficácia dos ajustes realizados.
