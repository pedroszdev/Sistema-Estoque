from os import system, name
import BancoDados

produtos=BancoDados.puxar_dados()

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
    nome=input('Digite o nome do novo produto: ').capitalize()
    quantidade=input('Digite a quantidade do novo produto: ')
    preco=input('Digite o preço desse novo produto: ')
    novos_produtos['Código']=int(codigo)
    novos_produtos['Nome']=nome.capitalize()
    novos_produtos['Quantidade']=int(quantidade)
    novos_produtos['Preço']=float(preco)
    produtos.append(novos_produtos)
    BancoDados.inserir_dados(novos_produtos)

def listar_produtos():
    if len(produtos)<1:
        print('Não existe produtos no momento')
    else:    
        print('-'*45)
        print('Código  | Nome        | Quantidade  | Preço')
        print('-'*45)
        for items in produtos:
            print(f'{items['Código']:<7} | {items['Nome']:<11} | '
                  f'{items['Quantidade']:<11} | {items['Preço']}')
        print('-'*45)
        print(f'Total de produtos cadastrados: {len(produtos)}')

def atualizar_produto():    
    resp=input('Qual produto você quer atualizar? [Nome] ').capitalize()
    
    for items in produtos:
        
        if resp==items['Nome']:
            atualizar_oque=input('O que você quer atualizar? ').capitalize()
            
            if atualizar_oque=='Código':
                codigo_novo=input('Digite o código novo: ')
                BancoDados.atualizar_codigo(items['Código'], codigo_novo)
                items['Código']=int(codigo_novo)

            
            elif atualizar_oque=='Nome':
                nome_novo=input('Digite o nome novo: ').capitalize()
                BancoDados.atualizar_nome(items['Nome'], nome_novo)
                items['Nome']=nome_novo

            
            elif atualizar_oque=='Quantidade':
                qnt_novo=input('Digite a quantidade nova: ')
                BancoDados.atualizar_quantidade(items['Quantidade'], qnt_novo)
                items['Quantidade']=int(qnt_novo)

            
            elif atualizar_oque=='Preço':
                preco_novo=input('Digite o novo preço: ')
                BancoDados.atualizar_preco(items['Preço'], preco_novo)
                items['Preço']=float(preco_novo)


            else:
                print('Essa categoria não existe')


def buscar_produto():
    resp=input('Qual produto você quer buscar? ').capitalize()
    try:
        resp=int(resp)
        for items in produtos:
            if resp==items['Código']:
                print(f'{items['Código']:<7} | {items['Nome']:<11} | '
                      f'{items['Quantidade']:<11} | {items['Preço']}')
                return
        else:
            print('Esse código não existe')
    except:
        for items in produtos:
            if resp==items['Nome']:
                print(f'{items['Código']:<7} | {items['Nome']:<11} | '
                      f'{items['Quantidade']:<11} | {items['Preço']}')
                return
        else:
            print('Esse produto não existe')

def remover_produto():
    resp=input('Qual produto você quer remover? [Nome] ').capitalize()
    for i, produto in enumerate(produtos):
        if resp==produto['Nome']:
            print(f'o {produto['Nome']} foi removido')
            del produtos[i]
            BancoDados.apagar_dados(produto['Nome'])
            return        
    else:
        print('Produto não encontrado. Nenhum item foi removido.')

def limpar_tela():
    if name == 'nt': 
        return system('cls')
    else:               
        return system('clear')