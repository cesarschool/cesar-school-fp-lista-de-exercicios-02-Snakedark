## QUESTÃO 4 ##
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos 
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o 
# valor da prestação como sendo o valor da casa a comprar dividido pelo número de 
# meses a pagar.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():

    # Programa que avalia a concessão de empréstimo para a compra de uma casa.

    valor_casa = float(input('Digite o valor da casa a comprar: '))
    salario = float(input('Digite seu salário: '))
    anos_a_pagar = float(input('Digite a quantidade de anos a pagar: '))
    prestacao = valor_casa / (anos_a_pagar * 12)
    if (prestacao > (salario * 0.30)):
        print('Empréstimo reprovado.')
    else:
        print('Empréstimo aprovado.')


if __name__ == '__main__':
    main()
