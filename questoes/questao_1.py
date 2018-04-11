## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():

    # Programa que lê cinco números inteiros e retorna o maior e o menor deles
    A = int(input('Digite o primeiro número: '))
    B = int(input('Digite o segundo número: '))
    C = int(input('Digite o terceiro número: '))
    D = int(input('Digite o quarto número: '))
    E = int(input('Digite o quinto número: '))

    # Condição para evitar igualdades

    if (A == B) or (A == C) or (A == D) or (A == E):
        print('Coloque números diferentes!')
    else:
        if (B == C) or (B == D) or (B == E):
            print('Coloque números diferentes!')
        else:
            if (C == D) or (C == E):
                print('Coloque números diferentes!')
            else:
                if (D == E):
                    print('Coloque números diferentes!')
                else:
                    if (A > B) and (A > C) and (A > D) and (A > E):
                        if (B < C) and (B < D) and (B < E):
                            print('Min: {0}\nMax: {1}'.format(B, A))
                        else:
                            if (C < D) and (C < E):
                                print('Min: {0}\nMax: {1}'.format(C, A))
                            else:
                                if (D < E):
                                    print('Min: {0}\nMax: {1}'.format(D, A))
                                else:
                                    print('Min: {0}\nMax: {1}'.format(E, A))
                    else:
                        if (B > C) and (B > D) and (B > E):
                            if (C < D) and (C < E) and (C < A):
                                print('Min: {0}\nMax: {1}'.format(C, B))
                            else:
                                if (D < E) and (D < A):
                                    print('Min: {0}\nMax: {1}'.format(D, B))
                                else:
                                    if (E < A):
                                        print('Min: {0}\nMax: {1}'.format(E, B))
                                    else:
                                        print('Min: {0}\nMax: {1}'.format(A, B))
                        else:
                            if (C > D) and (C > E):
                                if (D < E) and (D < A) and (D < B):
                                    print('Min: {0}\nMax: {1}'.format(D, C))
                                else:
                                    if (E < A) and (E < B):
                                        print('Min: {0}\nMax: {1}'.format(E, C))
                                    else:
                                        if (A < B):
                                            print('Min: {0}\nMax: {1}'.format(A, C))
                                        else:
                                            print('Min: {0}\nMax: {1}'.format(B, C))
                            else:
                                if (D > E):
                                    if (E < A) and (E < B) and (E < C):
                                        print('Min: {0}\nMax: {1}'.format(E, D))
                                    else:
                                        if (A < B) and (A < C):
                                            print('Min: {0}\nMax: {1}'.format(A, D))
                                        else:
                                            if (B < C):
                                                print('Min: {0}\nMax: {1}'.format(B, D))
                                            else:
                                                print('Min: {0}\nMax: {1}'.format(C, D))
                                else:
                                    if (A < B) and (A < C) and (A < D):
                                        print('Min: {0}\nMax: {1}'.format(A, E))
                                    else:
                                        if (B < C) and (B < D):
                                            print('Min: {0}\nMax: {1}'.format(B, E))
                                        else:
                                            if (C < D):
                                                print('Min: {0}\nMax: {1}'.format(C, E))
                                            else:
                                                print('Min: {0}\nMax: {1}'.format(D, E))


if __name__ == '__main__':
    main()