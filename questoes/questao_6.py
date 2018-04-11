## QUESTÃO 6 ##
# Escreva um programa que calcule a porcentagem de nucleotídeos A, C, G e T em 
# uma cadeia de DNA informada pelo usuário. Indicar também a quantidade e a 
# porcentagem de nucleotídeos inválidos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():

    # Programa que lê uma sequência de DNA e retorna a sua composição e quantidade de inválidos.

    sequencia = str(input('Digite a cadeia de DNA: ')).upper()
    Total = len(sequencia)
    A = (sequencia.count('A') / Total) * 100
    T = (sequencia.count('T') / Total) * 100
    C = (sequencia.count('C') / Total) * 100
    G = (sequencia.count('G') / Total) * 100
    invalido = 100 - (A + T + C + G)
    print('''Sequência total: {0}\n
           Adenina: {1}\n
           Timina: {2}\n
           Citosina: {3}\n
           Guanina: {4}\n
           Inválidos: {5}

           Porcentagens:\n
           Adenina: {6:.2f}\n
           Timina: {7:.2f}\n
           Citosina: {8:.2f}\n
           Guanina: {9:.2f}'''.format(Total, sequencia.count('A'), sequencia.count('T'), sequencia.count('C'),
                                      sequencia.count('G'), invalido, A, T, C, G))


if __name__ == '__main__':
    main()
