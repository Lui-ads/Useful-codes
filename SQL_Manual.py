# Essa é a versão 1.3 do SQL Manual, quando eu atualizar irei atualizar aqui no GitHub também

import time
import os

def escolha():
    print("""
Para ver o comando: 1
Para saber sua função: 2             
Para ver a sintaxe: 3""")
    acao = int(input("\nQual seu número: "))
    return acao
    
def select ():
    acao = escolha()
    
    comando = "SELECT"
    funcao = "Ele é usado para consultar e recuperar dados de uma ou mais tabelas"
    sintaxe = """
    SELECT coluna FROM nome_tabela;
    
    Exemplo 1: SELECT nome_cliente, email FROM clientes;
    
    Exemplo 2: SELECT * FROM clientes -- Esse seleciona tudo da tabela e mostra;
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def where ():
    acao = escolha()
    
    comando = "WHERE" 
    funcao = "Ele é usado para filtrar um registro em uma consulta SQL"
    sintaxe = """
    SELECT colunas FROM tabela WHERE condicao;
    
    Exemplo: SELECT * FROM clientes WHERE pais = ‘Brasil’;
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"

def distinct():
    acao = escolha()
    
    comando = "DISTINCT"
    funcao = "Ele remove duplicatas, em outras palavras ele evita redundâncias eliminando linhas duplicadas no resultado da consulta"
    sintaxe = """
    SELECT DISTINCT coluna FROM tabela;
    
    Exemplo: SELECT DISTINCT pais FROM clientes; # Aqui só vai ser mostrado uma vez cada País
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    

def creat_table ():
    acao = escolha()
    
    comando = "CREATE TABLE"
    funcao = "A função CREATE TABLE é usada para criação de tabelas"
    sintaxe = """
    CREATE TABLE nome_tabela ( 
    coluna1 tipo_de_dado restricoes, 
    coluna2 tipo_de_dado restricoes );
    
    Exemplo: 
        CREATE TABLE clientes (
            id INT PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(150) 
            );
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def alter_table():
    acao = escolha()

    comando = "ALTER TABLE"
    funcao = "Ele é usado para modificar a estrutura de uma tabela existente"
    sintaxe = """
    ALTER TABLE nome_tabela ADD coluna tipo;
    
    Exemplo 1: ALTER TABLE clientes ADD telefone VARCHAR(20);
    
    Exemplo 2: ALTER TABLE nome_da_tabela DROP COLUMN nome_da_coluna;
        # Nesse caso ele exclui a coluna pedida | CUIDADO! pois isso exclui permanentemente a coluna
        
    Obs.: Posso usar outras opções além do ADD, como o DROP etc...
    """

    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def drop_table():
    acao = escolha()
    
    comando = "DROP TABLE"
    funcao = "Ele exclui PERMANENTEMENTE uma tabela e todos os seus dados"
    sintaxe = """
    DROP TABLE nome_tabela;
    
    Exemplo: DROP TABLE clientes_backup;
    """                
                    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def pk():
    acao = escolha()
    
    comando = "PRIMARY KEY"
    funcao = "Define de forma única cada registro em uma tabela (não pode ter duas PK)"
    sintaxe = """
    coluna tipo PRIMARY KEY
    
    Exemplo 1: id INT PRIMARY KEY
    
    Exemplo 2: 
        CREATE TABLE alunos (
            CPF INT PRIMARY KEY,  -- Número único
            nome VARCHAR(100),
            email VARCHAR(200)
            );
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def fk():
    acao = escolha()
    
    comando = "FOREIGN KEY"
    funcao = "Ele é uma restrição que cria um vínculo entre duas tabelas"
    sintaxe = """
    FOREIGN KEY (coluna) REFERENCES outra_tabela(coluna);
    
    Exemplo 1: 
        CREATE TABLE pedidos ( 
            id INT PRIMARY KEY, 
            id_cliente INT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id) 
            );
            
    Exemplo 2:
        CREATE TABLE alunos (
            id_aluno INT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(200) UNIQUE,
            data_nascimento DATE
        ); 
        
        CREATE TABLE matriculas (
            id_matricula INT PRIMARY KEY,
            id_aluno INT,
            curso VARCHAR(100) NOT NULL,
            data_matricula DATE DEFAULT CURRENT_DATE,
            
            FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno)
            -- O id_aluno vem da tabela aluno, por isso referencia o id_aluno da tabela aluno
            );
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def insert_into():
    acao = escolha()
    
    comando = "INSERT INTO"
    funcao = "É usado para inserir novos registros a tabela"
    sintaxe = """
    INSERT INTO tabela (coluna1, coluna2) 
    VALUES  
        (valor1, valor2);
    
    Exemplo: 
        INSERT INTO produtos (id, nome, preco)
        VALUES 
            (1, 'Notebook', 2500.00),
            (2, 'Mouse', 50.00),
            (3, 'Teclado', 120.00);
        
        Obs.: Tudo que vai ser adicionado tem que estar na ordem que foi descrita, id, nome e preco 
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def insert_into_select():
    acao = escolha()
    
    comando = "INSERT INTO + SELECT"
    funcao = "Ele insere dados em uma tabela a partir do resultado de uma consulta SELECT feita em outra tabela (ou na própria)"
    sintaxe = """
    INSERT INTO nova_tabela (colunas) 
    SELECT colunas FROM tabela_origem 
    WHERE condicao;
    
    Exemplo comentado:
        -- Insere na tabela 'clientes_brasil' só os clientes do Brasil
        
        INSERT INTO clientes_brasil (id, nome, email) 
        
        -- Acha os clientes BR na tabela 'clientes'
        SELECT id, nome, email FROM clientes 
        
        -- Filtra somente oscom 'pais' igual a 'Brasil'
        WHERE pais = ‘Brasil’;

    Exemplo ńão comentado
        INSERT INTO clientes_brasil (id, nome, email) 
        SELECT id, nome, email FROM clientes 
        WHERE pais = ‘Brasil’;
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def operadores_de_comparacao():
    acao = escolha()
    
    comandos = "<, >, >=, >= e <>,"
    funcao = "Eles comparam coisas para ver qual é maior, menor, igual ou diferene"
    sintaxe = """
    algo <> algo_2
    
    Exemplo:
        SELECT * FROM pedidos WHERE valor > 200; 
        SELECT * FROM pedidos WHERE valor <> 200;

    """
    
    if acao == 1:
        return comandos
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def operadores_logicos():
    acao = escolha()
    
    comandos = "AND, NOT e OR"
    funcao = "Eles fazem a verificação lógica para poder validar uma verdade ou falsidade"
    sintaxe = """
    AND: condicao1 AND condicao2

    OR: condicao1 OR condicao2

    NOT: NOT condicao
    
    Exemplos:
        AND: SELECT * FROM pedidos WHERE valor > 200 AND status = ‘Pendente’;
        
        OR: SELECT * FROM pedidos WHERE status = ‘Pendente’ OR status = ‘Processando’;

        NOT: SELECT * FROM pedidos WHERE NOT status = ‘Cancelado’;
    """
    
    if acao == 1:
        return comandos
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def order_by():
    acao = escolha()
    
    comando = "ORDER BY"
    funcao = "Ele ordena os resultados das pesquisa em crescente (ASC) ou decrescente (DESC)."
    sintaxe = """
    SELECT colunas FROM tabela ORDER BY coluna DESC;
    SELECT colunas FROM tabela ORDER BY coluna ASC
    
    Exemplo:
        SELECT * FROM clientes ORDER BY nome ASC; 
        SELECT * FROM clientes ORDER BY id DESC;
    """
        
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def alias():
    acao = escolha()
    
    comando = "AS"
    funcao = "Ele da um nome temporário a colunas"
    sintaxe = """
    SELECT coluna AS apelido FROM tabela;
    
    Exemplo: SELECT email AS email_cliente FROM clientes;
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def update():
    acao = escolha()
    
    comando = "UPDATE"
    funcao = "Ele é usado para modificar dados existentes em uma ou mais linhas de uma tabela"
    sintaxe = """
    UPDATE tabela SET coluna = valor WHERE condicao;
    
    Exemplo: UPDATE clientes SET email = ‘novo@email.com’ WHERE id = 1;
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def delete():
    acao = escolha()
    
    comando = "DELETE"
    funcao = "Ele remove linhas de uma tabela"
    sintaxe = """
    DELETE FROM tabela WHERE condicao;
    
    Exemplo: DELETE FROM clientes WHERE id = 5;
    
    Obs.: Posso usar também o TUNCATE, ele é tipo um DELETE, mas sem possíbilidade de condições.
    """
    
    if acao == 1:
        return comando
    elif acao == 2:
        return funcao
    elif acao == 3:
        return sintaxe
    else:
        return "Escolha inválida"
    
def tipos():
    tipo = """
Texto (String):
    CHAR: Armazena strings de tamanho fixo. Usado quando os valores têm um comprimento constante
    VARCHAR: Armazena strings de tamanho variável. Apropriado para valores com comprimentos variáveis
    TEXTO (TEXT): Armazena strings muito longas, como documentos ou descrições

Numérico:
    INTEGER (INT): Armazena números inteiros
    FLOAT: Armazena números de ponto flutuante, geralmente usados para valores com casas decimais
    NUMERIC (DECIMAL): Armazena números com uma precisão específica, geralmente usados em aplicações financeiras

Data e Hora:
    DATE: Armazena datas sem informações de horário
    TIME: Armazena informações de horário
    TIMESTAMP: Combina data e horário em um único tipo

Booleano:
BOOLEAN (BOOL): Armazena valores verdadeiros ou falsos

Binário:
    BLOB (Binary Large Object): Armazena dados binários, como imagens, vídeos ou arquivos
    BIT: Armazena valores binários, como 0 ou 1

Obs.: Existem outros tipos, mas esses são os mais usados
    """

    return tipo
    
    
def subconjuntos():
    acao = int(input("""
Qual número você vai escolher:
1 - DDL
2 - DML
3 - DCL
4 - TCL          
Qual seu número: """))
    
    if acao == 1:
        resposta = """
DDL (Lida com a ESTRUTURA do banco de dados):
    Lida com a ESTRUTURA do banco de dados
        CREATE  - Cria bancos, tabelas, índices, views
        ALTER   - Modifica a estrutura existente
        DROP    - Remove completamente tabelas ou bancos
        TRUNCATE- Remove todos os dados mas mantém a estrutura
        RENAME  - Renomeia objetos (tabelas, colunas)
"""
        return resposta
    elif acao == 2:
        resposta = """
DML (DATA MANIPULATION LANGUAGE):
    Lida com os DADOS dentro das tabelas
        SELECT  - Consulta/recupera dados
        INSERT  - Adiciona novos registros
        UPDATE  - Modifica dados existentes
        DELETE  - Remove registros específicos
"""
        return resposta
    elif acao == 3:
        resposta = """
DCL (DATA CONTROL LANGUAGE): 
    Controla permissões e acesso
        GRANT   - Concede permissões
        REVOKE  - Remove permissões
"""
        return resposta
    elif acao == 4:
        resposta = """
TCL (TRANSACTION CONTROL LANGUAGE):
    Gerencia transações
        COMMIT    - Confirma alterações
        ROLLBACK  - Desfaz alterações
        SAVEPOINT - Cria ponto de restauração        
"""
        return resposta
    else:
        resposta = "Opção inválida"
        return resposta
    
def criacao():
    valor = False
    tabela = []
    fk_list = []  # Lista para guardar as FKs
    soma = 0
    print("\nVamos criar usa tabela :)\n")
    nome_tabela = input("Qual o nome da sua tabela: ")
    loop = int(input("\nQuantos atributos vai ter: "))
    
    # Pergunta sobre chaves estrangeiras
    qtd_fk = int(input("\nQuantas chaves estrangeiras (FK) vai ter: "))
    
    for i in range(loop):
        atriutos = []
        nome_atributo = input("\nNome do atributo: ")
        tipo = int(input("""
O atributo é de qual tipo: 

1 - Texto
2 - Numérico
3 - Data/hora
4 - Booleano
5 - Bináriao:

Qual seu número: """))

        if tipo == 1:
            usar = int(input("""
Qual devo usar:
1 - CHAR
2 - VARCHAR
3 - TEXT                  
Qual seu número: """))
            if usar == 1:
                tipo_str = "CHAR"
            elif usar == 2:
                tipo_str = "VARCHAR(250)"
            elif usar == 3:
                tipo_str = "TEXT"
            else:
                print("Erro")                 
        elif tipo == 2:
            usar = int(input("""
Qual devo usar:
1 - INT
2 - FLOAT 
3 - DECIMAL                            
Qual seu número: """))
            if usar == 1:
                tipo_str = "INT"
            elif usar == 2:
                tipo_str = "FLOAT"
            elif usar == 3:
                tipo_str = "DECIMAL"            
            else:
                print("Erro")

        elif tipo == 3:
            usar = int(input("""
Qual devo usar:
1 - DATE
2 - TIME
3 - TIMESTAMP                             
Qual seu número: """))
            if usar == 1:
                tipo_str = "DATE"
            elif usar == 2:
                tipo_str = "TIME"
            elif usar == 3:
                tipo_str = "TIMESTAMP"
            else:
                print("Erro")
        
        elif tipo == 4:        
                tipo_str = "BOOL"
        elif tipo == 5:
            usar = int(input("""
Qual devo usar:
1 - BLOB
2 - BIT
Qual seu número: """))
            if usar == 1:
                tipo_str = "BLOB"
            elif usar == 2:
                tipo_str = "LONGBLOB"
            
        else:
            print("Erro")
            
        definicao = f"{nome_atributo} {tipo_str}"
        
        if valor == False:
            pk_ou_nao = int(input("""
Seu atributo é uma chave primária (PK)
1 - Sim
2 - Não                              
Qual seu número: """))
            if pk_ou_nao == 1:
                definicao += " PRIMARY KEY"
                valor = True
            elif pk_ou_nao == 2:
                pass
            else:
                print("Erro")
        
        tabela.append(definicao)
    
    # Coleta as informações das FKs
    for j in range(qtd_fk):
        print(f"\n--- FK {j+1} ---")
        coluna_fk = input("Nome da coluna (na tabela atual): ")
        tabela_ref = input("Tabela referenciada: ")
        coluna_ref = input("Coluna referenciada: ")
        
        fk_string = f"FOREIGN KEY ({coluna_fk}) REFERENCES {tabela_ref}({coluna_ref})"
        fk_list.append(fk_string)
    
    # Junta colunas e FKs
    todas_definicoes = tabela + fk_list
    
    sql_final = f"CREATE TABLE {nome_tabela} (" + ", ".join(todas_definicoes) + ");"
    
    return sql_final  
    

# Software  
os.system("cls" if os.name == "nt" else "clear")
time.sleep(0.2)
while True:
    try:
        pulo = False
        print("""
Qual letra você vai escolher:

a - SELECT
b - WHERE
c - DISTINCT
d - CREATE TABLE      
e - ALTER TABLE
f - DROP TABLE
g - PRIMARY KEY
h - FOREIGN KEY
i - INSERT INTO
j - INSERT INTO + SELECT
k - Operadores de Comparação
l - Operadores Lógicos
m - ORDER BY
n - AS (ALIAS)
o - UPDATE
p - DELETE
q - Tipos
r - Subconjuntos

Para criar uma tabela com ajuda escreva: Criar
Para sair, digite: Sair

Obs.: Lembre que ao fazer um Banco de Dados em SQL o ; é muito importante para tudo funcionar, não esqueça deçe :)
            """)

        opcao = input("Qual letra vai ser: ")
        opcao = opcao.strip().lower()

        if opcao == "a":
            resultado = select()
        elif opcao == "b":
            resultado = where()
        elif opcao == "c":
            resultado = distinct()
        elif opcao == "d":
            resultado = creat_table()
        elif opcao == "e":
            resultado = alter_table()
        elif opcao == "f":
            resultado = drop_table()
        elif opcao == "g":
            resultado = pk()
        elif opcao == "h":
            resultado = fk()
        elif opcao == "i":
            resultado = insert_into()
        elif opcao == "j":
            resultado = insert_into_select()
        elif opcao == "k":
            resultado = operadores_de_comparacao()
        elif opcao == "l":
            resultado = operadores_logicos()
        elif opcao == "m":
            resultado = order_by()
        elif opcao == "n":
            resultado = alias()
        elif opcao == "o":
            resultado = update()
        
        elif opcao == "p":
            resultado = delete()
        
        elif opcao == "q":
            resultado = tipos()
        elif opcao == "r":
            resultado = subconjuntos()
        elif opcao == "criar":
            resultado = criacao()
        elif opcao == "limpar":
            os.system("cls" if os.name == "nt" else "clear")
            resultado = ""
            pulo = True
            time.sleep(0.2)
        elif opcao == "sair":
            time.sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
            print("\nFim\n")
            time.sleep(1)
            break
        else:
            resultado = "Escolha inválida"
            
        time.sleep(0.2)
        print(f"\n{resultado}\n")
        if pulo == False:
            input("De enter para voltar ao início\n\n")
        else:
            continue
    except:
        break
