import sqlite3
from pathlib import Path

PASTA_RAIZ=Path(__file__).parent
BD_NOME='Estoque.sqlite3'
BD_PASTA= PASTA_RAIZ / BD_NOME
NOME_TABELA='estoque'

conexao=sqlite3.connect(BD_PASTA)
cursor= conexao.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {NOME_TABELA} ('
    'Código INT NOT NULL, '
    'Nome VARCHAR(50) NOT NULL, '
    'Quantidade INT NOT NULL, '
    'Preço REAL NOT NULL, '
    'PRIMARY KEY (Código)'
    ')'
)

conexao.commit()
cursor.close()
conexao.close()

def inserir_dados(dados):
    conexao=sqlite3.connect(BD_PASTA)
    cursor= conexao.cursor()
    
    comando= (
        f'INSERT INTO {NOME_TABELA} '
        '(Código, Nome, Quantidade, Preço) '
        'VALUES '
        '(:Código, :Nome, :Quantidade, :Preço) '
    )

    cursor.execute(comando, dados)
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_codigo(codigo, codigo_novo):
    conexao=sqlite3.connect(BD_PASTA)
    cursor= conexao.cursor()
    
    comando=(
        f'UPDATE {NOME_TABELA} '
        'SET Código=? '
        'WHERE Código=? '
    )

    cursor.execute(comando,(codigo_novo,codigo))
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_nome(nome, nome_novo):
    conexao=sqlite3.connect(BD_PASTA)
    cursor= conexao.cursor()
    
    comando=(
        f'UPDATE {NOME_TABELA} '
        'SET Nome=? '
        'WHERE Nome=? '
    )

    cursor.execute(comando,(nome_novo, nome))
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_quantidade(qnt, qnt_novo):
    conexao=sqlite3.connect(BD_PASTA)
    cursor= conexao.cursor()
    
    comando=(
        f'UPDATE {NOME_TABELA} '
        'SET Quantidade=? '
        'WHERE Quantidade=? '
    )

    cursor.execute(comando,(qnt_novo, qnt))
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_preco(preco, preco_novo):
    conexao=sqlite3.connect(BD_PASTA)
    cursor= conexao.cursor()
    
    comando=(
        f'UPDATE {NOME_TABELA} '
        'SET Preço=? '
        'WHERE Preço=? '
    )

    cursor.execute(comando,(preco_novo, preco))
    conexao.commit()
    cursor.close()
    conexao.close()

def apagar_dados(nome):
    conexao=sqlite3.connect(BD_PASTA)
    cursor= conexao.cursor()
    
    comando=(
        f'DELETE FROM {NOME_TABELA} '
        'WHERE Nome=? '
    )

    cursor.execute(comando,(nome,))
    conexao.commit()
    cursor.close()
    conexao.close()

def puxar_dados():
    conexao=sqlite3.connect(BD_PASTA)
    conexao.row_factory = sqlite3.Row
    cursor= conexao.cursor()

    comando=(
        f'SELECT * FROM {NOME_TABELA} '
    )

    cursor.execute(comando)
    resultados=cursor.fetchall()
    Produtos = [dict(linha) for linha in resultados]

    return Produtos if len(Produtos)>=1 else []

