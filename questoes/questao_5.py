## QUESTÃO 5 ##
# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é 
# Equilátero, Isósceles ou Escaleno.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():

    # Programa que lê as medidas dos lados de um triângulo e diz se ele é Equilátero, Isósceles ou Escaleno.

    A = float(input('Digite o primeiro lado: '))
    B = float(input('Digite o segundo lado: '))
    C = float(input('Digite o terceiro lado: '))
    if (abs(A - B) < C < (A + B)) or (abs(A - C) < B < (A + C)) or (abs(B - C) < A < (B + C)):
        print('O triângulo existe.')
        if (A == B) and (A == C):
            print('O triângulo é Equilátero.')
        else:
            if (B == C):
                print('O triângulo é Isósceles.')
            else:
                print('O triângulo é Escaleno.')
    else:
        print('O triângulo não existe.')


if __name__ == '__main__':
    main()
