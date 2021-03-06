## QUESTÃO 7 ##
# A maioria dos anos tem 365 dias. No entanto, o tempo necessário para a Terra orbitar 
# o Sol é na verdade um pouco mais que isso. Como resultado, um dia extra, 29 de fevereiro, 
# está incluído em alguns anos para corrigir essa diferença. Esses anos são referidos como 
# anos bissextos. As regras para determinar se um ano é ou não um ano bissexto seguem:
# • Qualquer ano que seja divisível por 400 é um ano bissexto.
# • Dos anos restantes, qualquer ano que seja divisível por 100 não é um ano bissexto.
# • Dos anos restantes, qualquer ano que seja divisível por 4 é um ano bissexto.
# • Todos os outros anos não são anos bissextos.
# Escreva um programa que leia um ano do usuário e exiba uma mensagem indicando 
# se é ou não um ano bissexto.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():

    # Programa que lê um ano qualquer e diz se ele é bissexto ou não.

    Ano = int(input('Digite um ano qualquer: '))
    if ((Ano % 4) == 0):
        print('O ano é bissexto.')
    else:
        if ((Ano % 100) == 0):
            print('O ano não é bissexto.')
        else:
            if ((Ano % 400) == 0):
                print('O ano é bissexto.')
            else:
                print('O ano não é bissexto.')


if __name__ == '__main__':
    main()
