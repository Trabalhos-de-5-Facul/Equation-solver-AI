# Equation-solver-AI

### Trabalho academico estudando o algoritimo genético para resolver funções algébricas de primeiro grau

#### Gabriel Gonçalves Mattos Santini
#### Gustavo Melo Cacau
#### Henrique Victorino Dias
#### Lucas Rodrigues São João Miguel
#### Vinicius Rabelo Mancini


## Intruções para o funcionamento do programa

##### - É necessaria a instalação da biblioteca numpy (pip install numpy)
	
- Uma vez com o numpy intalado, execute o arquivo "main.py"
 
- Durante a execução, será pedido ao usuário a inserção de uma função polinomial e a mesma deve ser inserida seguindo algumas regras. Por exemplo:
- A expressão 3x^4+x^3-5x^2+46x-543 deverá ser digitada como: 
		
#### 				3 * x ** 4 + x ** 3 - 5 * x ** 2 + 46 * x - 543
			
	- Em resumo, o símbolo '^' que representa a elevação de um número por outro deverá ser substituido por '**'

	- O programa irá retornar aproximadamente as raizes desta função que seriam A = -4,15228364 e B = 3,40806689.
	- A principio o programa está configurado para retornas 2 resulados 
	- Outros exemplos simples para teste seriam x**2 + 2*x que tem como raiz -2 e 0 e 10 *x**2-5 *x-30 que tem como raiz -1.5 e 2
	- Para calculo da Raizes utilizamos do Geogebra
	
##### - Logo no Inicio do programa existe variavéis configuraveis para alterar o comportamento das populações e de suas mutações que são:
	- population_size -> Tamanho das populações
	- default_variation -> Variação inicial das mutações 
	- bests_sample_size -> Tamanho da amostra de análise para definir novos parametros de mutação 
	- bests_sample_use_size -> Tamanho da amostra para definir os novos melhores individuos e reproduzi-los e gerações futuras
	- start_sample -> Amostra Inicial para o ponto de partida 
	- qnt_results -> quantidade de resultados que devem ser tentado calcular 
	- max_repetitive_tries -> Quantas gerações repitidadas devem ter nenhuma mudança significativa para seu resultado ser considerado ótimo 
	- MAX_GENERATIONS -> Máximo de gerações que podem ser gerada 
	- result_variations -> Variação minima entre resultados anteriores
