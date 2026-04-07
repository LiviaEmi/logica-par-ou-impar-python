# operadores matemáticos
# somar +
# incrementar +=   ex: idade += 1 (pega a idade e soma com o número 1)
# subtração - 
# decremento -= ex: idade -= 1 (pega a idade e subtrai o número 1)
# multiplicação *
# divisão /          - ex: 3/2 = 1.5
# módulo %           - ex: 3%2 = 1 (traz o resto)
# igual ==
# diferente !=

# criando variáveis para o jogo
jogador1 = int(input('informe um número: '))
jogador2 = int(input('informe um número: '))

numero = jogador1 + jogador2
if numero % 2 != 0:
    print('ímpar ganhou')
else:
    print('par ganhou')