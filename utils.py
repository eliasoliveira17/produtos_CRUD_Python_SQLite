import sqlite3

def conectar():
    """
    Função para conectar ao servidor
    """
    conn = sqlite3.connect('pySQLite')

    conn.execute("""CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL    
    )""")
    return conn

def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()

def listar():
    """
    Função para listar os produtos
    """
    # Definição da conexão
    conn = conectar()
    # Definição do cursor
    cursor = conn.cursor()
    # Faz consulta de todo o conteúdo da tabela 'produto'
    cursor.execute('SELECT * FROM produtos')
    # Armazena os dados consultados
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos ...')
        print('---------------------')
        for produto in produtos:
                print(f"ID: {produto[0]}")
                print(f"Produto: {produto[1]}")
                print(f"Preço: {produto[2]}")
                print(f"Estoque: {produto[3]}")
                print('---------------------')
    else:
        print("Não existem produtos a serem listados!")
    
    desconectar(conn)

def inserir():
    """
    Função para inserir um produto
    """ 
    # Definição da conexão 
    conn = conectar()
    # Definição do cursor
    cursor = conn.cursor()

    print('Inserindo produto ...')
    print('---------------------')
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    estoque = int(input("Informe a quantidade de produtos em estoque: "))

    cursor.execute(f"INSERT INTO produtos(nome, preco, estoque) VALUES ('{nome}',{preco},{estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O produto {nome} foi inserido no banco de dados com sucesso.")
        print('---------------------')
    else:
        print("Não foi possível inserir o produto.")
        print('---------------------')

    desconectar(conn)

def atualizar():
    """
    Função para atualizar um produto
    """
    # Definição da conexão
    conn = conectar()
    # Definição do cursor
    cursor = conn.cursor()

    print('Atualizando produto ...')
    print('---------------------')

    _id = int(input('Informe o ID do produto: '))
    nome = input('Informe o nome atualizado do produto: ')
    preco = float(input('Informe o preço atualizado do produto: '))
    estoque = int(input('Informe a quantidade atualizada de produtos em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco = {preco}, estoque={estoque} WHERE id = {_id}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado  no banco de dados com sucesso.')
        print('---------------------')
    else:
        print('Não foi possível atualizar o produto.')
        print('---------------------')

    desconectar(conn)

def deletar():
    """
    Função para deletar um produto
    """  
    # Definição da conexão
    conn = conectar()
    # Definição do cursor
    cursor = conn.cursor()

    print('Deletando produtos ...')
    print('---------------------')

    _id = int(input('Informe o ID do produto a ser deletado: '))

    cursor.execute(f'DELETE FROM produtos WHERE id = {_id}')
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto com ID = {_id} foi deletado do banco de dados com sucesso.')
        print('---------------------')
    else:
        print(f'Não foi possível excluir o produto com ID = {_id}.')
        print('---------------------')

    desconectar(conn)

def menu():
    """
    Função para gerar o menu inicial
    """
    # Operações disponíveis no menu
    operacoesTxt = ['Listar produtos.', 'Inserir produto.', 'Atualizar produto.', 'Deletar produto.', 'Sair.']
    # Extração de nomes das funções correspondentes
    operacoes = [operacao.split()[0].lower() for operacao in operacoesTxt]
    # Formatação de exibição de texto das operações disponíveis no menu
    operacoesTxt = [str(it+1) + ' - ' + operacoesTxt[it] for it in range(0,len(operacoesTxt))]
    
    opcao = 0
    # Loop para seleção de operações no menu pelo usuário
    while(opcao != len(operacoesTxt)):
        #  Prints das operações dispníveis no terminal
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        for operacaoTxt in operacoesTxt:
            print(operacaoTxt)
        # Coleta da operação desejada pelo usuário
        opcao = int(input())
        # Chamada das funções desejadas pelo usuário
        if opcao != len(operacoesTxt):
            globals()[operacoes[opcao-1]]()
        # Encerramento do loop 
        elif opcao == len(operacoesTxt):
                print('*** Saindo ***')
        else:
            print('*** Opção inválida ***')
