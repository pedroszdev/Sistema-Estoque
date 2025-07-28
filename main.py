from time import sleep
import funcoes

while True:
    funcoes.menu()
    resp=input('Escolha uma opção: ')
    funcoes.limpar_tela()
    if resp=='1':
        funcoes.cadastrar_produto()
    elif resp=='2':
        funcoes.listar_produtos()
    elif resp=='3':
        funcoes.atualizar_produto()
    elif resp=='4':
        funcoes.buscar_produto()
    elif resp=='5':
        funcoes.remover_produto()
    elif resp=='6':
        break
    else:
        print('Você digitou a opção errada')
    sleep(0.5)    