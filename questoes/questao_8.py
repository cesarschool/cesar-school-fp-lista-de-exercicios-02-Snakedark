## QUESTÃO 8 ##
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    # Programa que lê a data e retorna a data do dia seguinte.

    Ano = int(input('Digite o ano atual: '))

    # Verificação se o ano é bissexto ou não:

    if ((Ano % 4) == 0):
        Bissexto = True
    elif ((Ano % 100) == 0):
        Bissexto = False
    elif ((Ano % 400) == 0):
        Bissexto = True
    elif ((Ano % 400) != 0):
        Bissexto = False

    Mes = int(input('Digite o número do mês: '))
    Dia = int(input('Digite o dia: '))
    print('A data atual é: {0}-{1}-{2}'.format(Dia, Mes, Ano))

    # Cálculo para o caso do ano ser bissexto:

    if (Bissexto == True):
        if (Mes == 1) or (Mes == 3) or (Mes == 5) or (Mes == 7) or (Mes == 8) or (Mes == 10) or (Mes == 12):
            if (Dia == 31):
                Dia = 1
                if (Mes == 12):
                    Mes = 1
                    Ano = Ano + 1
                else:
                    Mes = Mes + 1
            else:
                Dia = Dia + 1
        else:
            if (Dia == 29) and (Mes == 2):  # Para o mês de Fevereiro
                Dia = 1
                Mes = Mes + 1
            else:
                if (Dia == 30):
                    Dia = 1
                    Mes = Mes + 1
                else:
                    Dia = Dia + 1
                    print('A data seguinte é: {0}-{1}-{2}'.format(Dia, Mes, Ano))
    else:
        if (Dia == 31):
            Dia = 1
            if (Mes == 12):
                Mes = 1
                Ano = Ano + 1
            else:
                Mes = Mes + 1
        else:
            if (Dia == 28) and (Mes == 2):  # Para o mês de Fevereiro
                Dia = 1
                Mes = Mes + 1
            else:
                if (Dia == 30):
                    Dia = 1
                    Mes = Mes + 1
                else:
                    Dia = Dia + 1
                    print('A data seguinte é: {0}-{1}-{2}'.format(Dia, Mes, Ano))


if __name__ == '__main__':
    main()
