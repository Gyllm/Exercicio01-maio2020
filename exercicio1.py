import os
import time


def cls():
  os.system('cls' if os.name=='nt' else 'clear')


cls()
op=1
menu = ('''[1] - Cadastrar Pessoa
[2] - Mostrar pessoas cadastradas
[0] - Sair do programa ''')
while op != 0:
    cls()
    print(40 * '=')
    print(menu)
    print(40 * '=')
    try:
        op = int(input())
    except ValueError:
        print('Erro! Você deve digitar o número correspondente a opção escolhida')
        time.sleep(3)
    else:
        if op==0:
            print(40 * '=')
            print('Sair do programa')
            print(40 * '=')
            cls()
            break
        elif op==1:
            # Cadastrar Pessoa
            cls()
            print(40 * '=')
            nome = input('Digite o nome da pessoa ')
            nome=nome.title()
            try:
                idade = int(input('Digite a idade da pessoa '))
                print(40 * '=')
            except ValueError:
                print('Erro! A idade da pessoa deve ser um número inteiro')
                time.sleep(3)
            else:
                arquivo = open('cadastro.txt', 'r')
                conteudo = arquivo.readlines()
                dados = nome + '   ' + str(idade) + '\n'
                conteudo.append(dados)
                arquivo = open('cadastro.txt', 'w')
                arquivo.writelines(conteudo)
                arquivo.close()
                print('Usuário cadastrado com sucesso')
                print(40 * '=')
                time.sleep(1)
        elif op==2:
            # Mostrar pessoas cadastradas
            cls()
            print(40 * '=')
            print('PESSOAS CADASTRADAS')
            arquivo = open('cadastro.txt', 'r')
            pessoal = arquivo.read()
            arquivo.close()
            print(pessoal)
            print(40 * '=')
            time.sleep(5)
        else:
            #Opção inválida
            print(40 * '=')
            print('Você escolheu uma opção inválida')
            print(40 * '=')
            time.sleep(2)
    