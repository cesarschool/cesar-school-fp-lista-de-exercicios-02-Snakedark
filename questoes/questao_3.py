## QUESTÃO 3 ##
# Implementar um programa que calcula o desconto previdenciário de um funcionário. 
# O programa deve, dado um salário, retornar o valor do desconto proporcional ao mesmo. 
# O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário, entretanto, 
# o valor máximo de desconto é 318,20.
# Sendo assim, ou o programa retorna 11% sobre o salário ou 318,20.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():

    # Programa que calcula o desconto previdenciário de uma pessoa e retorna o valor do desconto.

    salario = float(input('Digie seu salário: '))
    desconto = salario * 0.11
    if (desconto <= 318.20):
        print('O valor do desconto é: {0:.2f}'.format(desconto))
    else:
        print('O valor do desconto é 318.20')


if __name__ == '__main__':
    main()
