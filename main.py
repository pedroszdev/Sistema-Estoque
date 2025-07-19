def menu():
    print('==== SISTEMA DE ESTOQUE ====')
    print('1- Cadastrar produto')
    print('2- Listar produtos')
    print('3- Atualizar produtos')
    print('4- Buscar produto')
    print('5- Remover produto')
    print('6- Sair')
    print('-'*30)

def cadastrar_produto():
    novos_produtos={}
    codigo=input('Digite o código do novo produto:')
    nome=input('Digite o nome do novo produto: ')
    quantidade=input('Digite a quantidade do novo produto')
    preco=input('Digite o preço desse novo produto: ')
    novos_produtos['Código']=int(codigo)
    novos_produtos['Nome']=nome
    novos_produtos['Quantidade']=int(quantidade)
    novos_produtos['Preço']=float(preco)
    produtos.append(novos_produtos)

def listar_produtos():
    print('-'*45)
    print('Código  | Nome        | Quantidade  | Preço')
    print('-'*45)
    for items in produtos:
        print(f'{items['Código']:<7} | {items['Nome']:<11} | {items['Quantidade']:<11} | {items['Preço']}')

def atualizar_produto():
    resp=input('Qual produto você quer atualizar? [Nome] ')
    for items in produtos:
        if items['Nome']==resp:
            atualizar_oque=input('O que você quer atualizar? ').capitalize()
            if atualizar_oque=='Código':
                codigo_novo=input('Digite o código novo: ')
                items['Código']=int(codigo_novo)
            elif atualizar_oque=='Nome':
                nome_novo=input('Digite o nome novo: ')
                items['Nome']=nome_novo
            elif atualizar_oque=='Quantidade':
                qnt_novo=input('Digite a quantidade nova: ')
                items['Quantidade']=int(qnt_novo)
            elif atualizar_oque=='Preço':
                preco_novo=input('Digite o novo preço: ')
                items['Preço']=float(preco_novo)
            else:
                print('Essa categoria não existe')

def buscar_produto():
    resp=input('Qual produto você quer buscar? ').capitalize()
    try:
        resp=int(resp)
        for items in produtos:
            if resp==items['Código']:
                print(f'{items['Código']:<7} | {items['Nome']:<11} | {items['Quantidade']:<11} | {items['Preço']}')
            else:
                print('Esse código não existe')
    except:
        for items in produtos:
            if resp==items['Nome']:
                print(f'{items['Código']:<7} | {items['Nome']:<11} | {items['Quantidade']:<11} | {items['Preço']}')
            else:
                print('Esse produto não existe')

def remover_produto():
    resp=input('Qual produto você quer remover? [Nome] ').capitalize()
    for items in produtos:
        if resp==items['Nome']:
            del items

produtos=[]


while True:
    menu()
    resp=input('Escolha uma opção: ')
    if resp=='1':
        cadastrar_produto()
    elif resp=='2':
        listar_produtos()
    elif resp=='3':
        atualizar_produto()
    elif resp=='4':
        buscar_produto()
    elif resp=='5':
        remover_produto()
    elif resp=='6':
        break
    else:
        print('Você digitou a opção errada')
        continue