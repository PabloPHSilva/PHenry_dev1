# 1.ProjetoGraduação_1
import random

values = ['P','T','R']
novamente = True

def Humano(forma):
    if forma == 'P' or forma == 'p':
        valor = 'Papel'

    elif forma == 'T' or forma == 't':
        valor = 'Tesoura'

    elif forma == 'R' or forma == 'r':
        valor = 'Pedra'
        
    elif forma != 'P' and forma != 'p' and forma != 'R' and forma != 'r' and forma != 'T' and forma != 't':
        valor = 'Nenhum'

    return valor

def CPU(forma2):
    if forma2 == 'P':
        valor2 = 'Papel'

    elif forma2 == 'T':
        valor2 = 'Tesoura'

    elif forma2 == 'R':
        valor2 = 'Pedra'

    return valor2


while novamente == True:
    x = random.randint(0,2)

    forma = input("Insira 'P' para Papel, 'T' para Tesoura, 'R' para Pedra: \n")

    forma2 = values[x]
    print(f'Computador {CPU(forma2)}, e Você {Humano(forma)}\n')

    if CPU(forma2) == Humano(forma):
        print('Empate!!!!\n')

    elif CPU(forma2)=='Tesoura' and Humano(forma)=='Papel':
        print('VOCÊ PERDEEEEU, CPU VENCEUUUU!!!\n')

    elif CPU(forma2) == 'Papel' and Humano(forma) == 'Pedra':
        print('VOCÊ PERDEEEEU, CPU VENCEUUUU!!!\n')

    elif CPU(forma2) == 'Pedra' and Humano(forma) == 'Tesoura':
        print('VOCÊ PERDEEEEU, CPU VENCEUUUU!!!\n')

    elif Humano(forma)=="Nenhum":
        print('PERDEU de WO, Há Há Há !!!!\n')


    else:
        print('VOCÊ VENCEU!!!!\n')

    print('Deseja jogar novamente?')
    novamente = input ('Insira "S" para Sim e "N" para Não:  ')
    if novamente == "n" or novamente == "N":
        novamente = False
        print ()
    else:
        novamente = True
        print ()
