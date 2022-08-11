"""
Variáveis são lugares reservados na memória de um dispositivo para o armazenamento dados.
1º Não se pode iniciar a variável com um número.
2º Pode conter números, mas não no inicio.
3º Para dar espaço é com _
4º É recomendável utilizar letras minúsculas.
"""
nome = 'Deivid Andrade'
idade = 31
altura = 1.72
e_maior = idade > 18
peso = 65
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))


