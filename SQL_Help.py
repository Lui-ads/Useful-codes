# Essa é a versão 1.5 do SQL Help

import time
import os

def escolha():
    print("""
Para ver o comando: 1
Para saber sua função: 2             
Para ver a sintaxe: 3""")
    acao = input("\nQual seu número: ")
    return acao
       
def select():
    acao = escolha()
    
    comando = "SELECT"
    funcao = "Ele é usado para consultar e recuperar dados de uma ou mais tabelas"
    sintaxe = """
    SELECT coluna FROM nome_tabela;
    
    Exemplo 1: SELECT nome_cliente, email FROM clientes;
    
    Exemplo 2: SELECT * FROM clientes -- Esse seleciona tudo da tabela e mostra;
    
    Obs.: Na consulta na dúvida use aspas simples '' quando for comparar com um String
    """
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def where():
    acao = escolha()
    
    comando = "WHERE" 
    funcao = "Ele é usado para filtrar um registro em uma consulta SQL"
    sintaxe = """
    SELECT colunas FROM tabela WHERE condicao;
    
    Exemplo: SELECT * FROM clientes WHERE pais = 'Brasil';
    """
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"

def distinct():
    acao = escolha()
    
    comando = "DISTINCT"
    funcao = "Ele remove duplicatas, em outras palavras ele evita redundâncias eliminando linhas duplicadas no resultado da consulta"
    sintaxe = """
    SELECT DISTINCT coluna FROM tabela;
    
    Exemplo: SELECT DISTINCT pais FROM clientes; -- Aqui só vai ser mostrado uma vez cada País
    """
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
        
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def fron():
    acao = escolha()
    
    comando = "FROM"
    funcao = "FROM: Cria uma tabela virtual temporária a partir de uma subconsulta para ser usada na consulta principal"
    sintaxe = """
FROM:
    SELECT colunas
    FROM (SELECT subconsulta) AS nome_tabela_virtual
    WHERE condições;
    
Exemplo 1:
    -- Média de vendas por categoria (apenas médias > 100)
    SELECT categoria, media_vendas
    FROM (
        SELECT categoria, AVG(valor) AS media_vendas
        FROM produtos
        GROUP BY categoria
    ) AS resumo_categorias
    WHERE media_vendas > 100;

Exemplo 2:
    -- Total de vendas por mês
    SELECT mes, total_mes
    FROM (
        SELECT MONTH(data) AS mes, SUM(valor) AS total_mes
        FROM vendas
        GROUP BY MONTH(data)
    ) AS vendas_mensais
    ORDER BY mes;

Obs.: Sobre tabela.coluna:
    Quando você vê algo como 'clientes.nome', significa: 
        PRIMEIRO vem o nome da TABELA (clientes), DEPOIS vem um PONTO (.) e por ÚLTIMO vem o nome da COLUNA (nome)
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
        
        -- Filtra somente os com 'pais' igual a 'Brasil'
        WHERE pais = 'Brasil’;

    Exemplo não comentado
        INSERT INTO clientes_brasil (id, nome, email) 
        SELECT id, nome, email FROM clientes 
        WHERE pais = 'Brasil’;
    """
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def update():
    acao = escolha()
    
    comando = "UPDATE"
    funcao = "Ele é usado para modificar dados existentes em uma ou mais linhas de uma tabela"
    sintaxe = """
    UPDATE tabela SET coluna = valor WHERE condicao;
    
    Exemplo: UPDATE clientes SET email = 'novo@email.com’ WHERE id = 1;
    """
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
    
    Obs.: Posso usar também o TRUNCATE, ele é tipo um DELETE, mas sem possibilidade de condições.
    """
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def create_table():
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
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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

    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
                    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
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
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def operadores_de_comparacao():
    acao = escolha()
    
    comandos = "=, <, >, <=, >=, <>"
    funcao = "Eles comparam coisas para ver qual é maior, menor, igual ou diferente"
    sintaxe = """
    algo_1 = algo_2
    algo_4 < algo_5
    algo_6 > algo_5
    algo_7 <= algo_8
    algo_9 >= algo_10
    algo_11 <> algo_12
    
    Exemplo:
        SELECT * FROM pedidos WHERE valor > 200; 
        SELECT * FROM pedidos WHERE valor <> 200;

    Obs.: O * é um Operador_Coringa / Wildcard que representa TUDO ou TODOS OS ELEMENTOS em determinado contexto
    """
    
    if acao == "1":
        return comandos
    elif acao == "2":
        return funcao
    elif acao == "3":
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
        AND: SELECT * FROM pedidos WHERE valor > 200 AND status = 'Pendente’;
        
        OR: SELECT * FROM pedidos WHERE status = 'Pendente’ OR status = 'Processando’;

        NOT: SELECT * FROM pedidos WHERE NOT status = 'Cancelado’;
        
    Obs.: O * é um Operador_Coringa / Wildcard que representa TUDO ou TODOS OS ELEMENTOS em determinado contexto
    """
    
    if acao == "1":
        return comandos
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def tipos():
    tipo = """
Texto (String):
    CHAR: Armazena strings de tamanho fixo. Usado quando os valores têm um comprimento constante
    VARCHAR: Armazena strings de tamanho variável. Apropriado para valores com comprimentos variáveis
    TEXT: Armazena strings muito longas, como documentos ou descrições
    
    Obs.: Na consulta na dúvia use aspas simples ''

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
    
def agregacoes():
    resposta = """
As agregações são:
    COUNT()  - Conta linhas
    SUM()    - Soma valores numéricos
    AVG()    - Calcula a média
    MAX()    - Retorna o maior valor
    MIN()    - Retorna o menor valor

Funções de arredondamento:
    ROUND()  - Arredonda números para casas decimais específicas
    CEIL()   - Arredonda para cima (teto)
    FLOOR()  - Arredonda para baixo (chão)    
    
Exemplos de agregações:

    COUNT(*): SELECT COUNT(*) FROM clientes;
    COUNT(coluna): SELECT COUNT(email) FROM clientes;
    COUNT(DISTINCT): SELECT COUNT(DISTINCT pais) FROM clientes;

    SUM: SELECT SUM(valor) FROM pedidos;
    AVG: SELECT AVG(valor) FROM pedidos;
    MAX: SELECT MAX(valor) FROM pedidos;
    MIN: SELECT MIN(valor) FROM pedidos;

Exemplos com ROUND, CEIL e FLOOR:
    SELECT 
        nome_produto,
        preco,
        ROUND(preco, 0) AS preco_inteiro,
        ROUND(preco * 1.1, 2) AS preco_com_imposto
    FROM produtos;
    
    SELECT 
        pedido_id,
        dias_para_entrega,
        CEIL(dias_para_entrega) AS dias_uteis_necessarios
    FROM pedidos;
    
    SELECT 
        nome,
        data_nascimento,
        FLOOR(DATEDIFF(CURDATE(), data_nascimento) / 365) AS idade_anos_completos
    FROM clientes;
    
    """
    return resposta

def subconjuntos():
    acao = int(input("""
Qual número você vai escolher:
1 - Função dos Subconjuntos
2 - DDL
3 - DML
4 - DCL
5 - TCL          
Qual seu número: """))
    
    if acao == 1:
        resposta = """
As funções de subconjuntos fazem parte das funções de agregação, mas com um comportamento específico:
    Elas operam em subconjuntos de dados definidos por filtros ou condições  
"""
        return resposta
    elif acao == 2:
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
    elif acao == 3:
        resposta = """
DML (DATA MANIPULATION LANGUAGE):
    Lida com os DADOS dentro das tabelas
        SELECT  - Consulta/recupera dados
        INSERT  - Adiciona novos registros
        UPDATE  - Modifica dados existentes
        DELETE  - Remove registros específicos
"""
        return resposta
    elif acao == 4:
        resposta = """
DCL (DATA CONTROL LANGUAGE): 
    Controla permissões e acesso
        GRANT   - Concede permissões
        REVOKE  - Remove permissões
"""
        return resposta
    elif acao == 5:
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
    
def join():
    acao = escolha()
    
    comando = "JOIN"
    funcao = "JOIN combina registros de duas ou mais tabelas com base em uma coluna relacionada entre elas"
    sintaxe = """
INNER JOIN:
    SELECT colunas
    FROM tabela1
    INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
    
    Exemplo:
        SELECT clientes.nome, pedidos.produto, pedidos.valor
        FROM clientes
        INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;
    
LEFT JOIN:
    SELECT colunas
    FROM tabela1
    LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
    
    Exemplo:
        SELECT clientes.nome, pedidos.produto, pedidos.valor
        FROM clientes
        LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
    
RIGHT JOIN:
    SELECT colunas
    FROM tabela1
    RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
    
    Exemplo:
        SELECT clientes.nome, pedidos.produto, pedidos.valor
        FROM clientes
        RIGHT JOIN pedidos ON clientes.id = pedidos.cliente_id;

FULL JOIN:
    SELECT colunas
    FROM tabela1
    FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

    Exemplo:
        SELECT clientes.nome, pedidos.produto, pedidos.valor
        FROM clientes
        FULL JOIN pedidos ON clientes.id = pedidos.cliente_id;

CROSS JOIN:
    SELECT colunas
    FROM tabela1
    CROSS JOIN tabela2;
    
    Exemplo:
        SELECT clientes.nome, pedidos.produto
        FROM clientes
        CROSS JOIN pedidos;
        
Obs.: Sobre tabela.coluna:
    Quando você vê algo como 'clientes.nome', significa: 
        PRIMEIRO vem o nome da TABELA (clientes), DEPOIS vem um PONTO (.) e por ÚLTIMO vem o nome da COLUNA (nome)
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def group_by():
    acao = escolha()
    comando = "GROUP BY"
    funcao = "Ele agrupa linhas que têm os mesmos valores em colunas especificadas para usar funções de agregação"
    sintaxe = """
SELECT coluna, função_agregação(coluna)
FROM tabela
GROUP BY coluna;

Exemplo 1:
    -- Contar quantos clientes por país
    SELECT pais, COUNT(*) AS total_clientes
    FROM clientes
    GROUP BY pais;
    
Exemplo 2:
    -- Somar vendas por categoria
    SELECT categoria, SUM(valor) AS total_vendas
    FROM produtos
    GROUP BY categoria;
    
Exemplo 3:
    -- Média de preço por departamento
    SELECT departamento, AVG(preco) AS media_preco
    FROM produtos
    GROUP BY departamento; 

Exemplo 4:
    -- Maior salário por cargo
    SELECT cargo, MAX(salario) AS maior_salario
    FROM funcionarios
    GROUP BY cargo;

Exemplo 5:
    -- Múltiplas colunas (cidade e estado)
    SELECT estado, cidade, COUNT(*) AS total
    FROM clientes
    GROUP BY estado, cidade;   
""" 
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
        
def having():
    acao = escolha()
    
    comando = "HAVING"
    funcao = "Filtra grupos criados pelo GROUP BY (como WHERE, mas para grupos, não para linhas individuais)"
    sintaxe = """
SELECT coluna, função_agregação(coluna)
FROM tabela
GROUP BY coluna
HAVING condição_do_grupo;

Exemplo 1:
    -- Países com mais de 10 clientes
    SELECT pais, COUNT(*) AS total_clientes
    FROM clientes
    GROUP BY pais
    HAVING COUNT(*) > 10;

Exemplo 2:
    -- Categorias com venda total acima de R$ 1000
    SELECT categoria, SUM(valor) AS total_vendas
    FROM produtos
    GROUP BY categoria
    HAVING SUM(valor) > 1000;

Exemplo 3:
    -- Departamentos com média salarial acima de 5000
    SELECT departamento, AVG(salario) AS media_salario
    FROM funcionarios
    GROUP BY departamento
    HAVING AVG(salario) > 5000;

Exemplo 4:
    -- Produtos com menos de 5 unidades em estoque
    SELECT produto, SUM(quantidade) AS estoque_total
    FROM estoque
    GROUP BY produto
    HAVING SUM(quantidade) < 5;

"""

    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def sub_correla():
    acao = escolha()

    comando = "WHERE e FROM"
    funcao = "Subconsulta que referencia colunas da consulta externa, executada para cada linha da consulta principal"
    sintaxe = """
SELECT colunas
FROM tabela_principal AS alias1
WHERE coluna OPERADOR (SELECT subconsulta 
                    FROM tabela_secundaria AS alias2 
                    WHERE alias2.coluna = alias1.coluna);

Exemplo 1:
-- Funcionários com salário acima da média do seu departamento
SELECT f1.nome, f1.salario, f1.departamento
FROM funcionarios f1
WHERE salario > (
    SELECT AVG(salario)
    FROM funcionarios f2
    WHERE f2.departamento = f1.departamento
);

Exemplo 2:
-- Clientes com mais de 5 pedidos
SELECT c.nome, c.email
FROM clientes c
WHERE (
    SELECT COUNT(*)
    FROM pedidos p
    WHERE p.cliente_id = c.id
) > 5;     
"""
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def limit():
    acao = escolha()
    
    comando = "LIMIT"
    funcao = "Limita a quantidade de registros retornados em uma consulta"
    sintaxe = """
SELECT colunas
FROM tabela
LIMIT numero_de_linhas;

Exemplo 1:
    -- Os 10 primeiros clientes
    SELECT nome, email
    FROM clientes
    LIMIT 10;

Exemplo 2:
    -- Os 5 produtos mais caros
    SELECT nome, preco
    FROM produtos
    ORDER BY preco DESC
    LIMIT 5;

Exemplo 3:
    -- Os 3 funcionários mais novos
    SELECT nome, data_contratacao
    FROM funcionarios
    ORDER BY data_contratacao DESC
    LIMIT 3; 
"""
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
        
def offset():
    acao = escolha()
    
    comando = "OFFSET"
    funcao = "Pula um número específico de linhas antes de começar a retornar os resultados"
    sintaxe = """
SELECT colunas
FROM tabela
LIMIT numero_de_linhas OFFSET numero_para_pular;

Exemplo 1:
    -- Pula os 5 primeiros e mostra os próximos 10
    SELECT nome, email
    FROM clientes
    LIMIT 10 OFFSET 5;

Exemplo 2:
    -- Página 2 (registros 11-20) de clientes ordenados
    SELECT nome, email
    FROM clientes
    ORDER BY nome
    LIMIT 10 OFFSET 10;

Exemplo 3:
    -- Página 3 (registros 21-30) dos produtos mais caros
    SELECT nome, preco
    FROM produtos
    ORDER BY preco DESC
    LIMIT 10 OFFSET 20;    
"""
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def limit_and_offset():
    acao = escolha()
    comando = "LIMIT com OFFSET (forma abreviada)"
    funcao = """
Limita a quantidade de registros retornados em uma consulta, pulando um número específico de linhas antes de começar a mostrar os resultados
"""
    sintaxe = """
SELECT colunas
FROM tabela
LIMIT offset, quantidade;

Exemplo 1:
    SELECT nome, preco, categoria
    FROM produtos
    ORDER BY nome
    LIMIT 10 OFFSET 0;

Exemplo 2:
    SELECT nome, preco, categoria
    FROM produtos
    ORDER BY nome
    LIMIT 10 OFFSET 10;

Exemplo 3:
    SELECT nome, preco, categoria
    FROM produtos
    ORDER BY nome
    LIMIT 10 OFFSET 20;
"""    

    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def not_null():
    acao = escolha()
    comando = "NOT NULL"
    funcao = "Garante que uma coluna não possa ter valores nulos (vazios), ou seja, é obrigatório preencher"
    sintaxe = """
    
-- Na criação da tabela
CREATE TABLE tabela (
    coluna tipo NOT NULL
);

-- Ou adicionando depois
ALTER TABLE tabela
MODIFY coluna tipo NOT NULL;

Exemplo 1:
    CREATE TABLE clientes (
        id INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(150) NOT NULL,
        telefone VARCHAR(20)  -- Pode ser nulo
    );

Exemplo 2:
    CREATE TABLE produtos (
        id INT PRIMARY KEY,
        nome VARCHAR(200) NOT NULL,
        preco DECIMAL(10,2) NOT NULL,
        descricao TEXT
    );

Exemplo 3:
    ALTER TABLE clientes
    MODIFY telefone VARCHAR(20) NOT NULL;
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"

def unique():
    acao = escolha()
    comando = "UNIQUE"
    funcao = "Garante que todos os valores em uma coluna sejam diferentes (não podem se repetir)"
    sintaxe = """  
-- Na criação da tabela
CREATE TABLE tabela (
    coluna tipo UNIQUE
);

-- Ou como restrição separada
CREATE TABLE tabela (
    coluna tipo,
    CONSTRAINT nome_restricao UNIQUE (coluna)
);

Exemplo 1:
    CREATE TABLE clientes (
        id INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        cpf VARCHAR(11) UNIQUE
    );

Exemplo 2:
    CREATE TABLE telefones (
        id INT PRIMARY KEY,
        cliente_id INT,
        numero VARCHAR(20),
        CONSTRAINT unique_telefone_cliente UNIQUE (cliente_id, numero)
    );

Exemplo 3:
    ALTER TABLE clientes
    ADD CONSTRAINT unique_cpf UNIQUE (cpf);
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def default():
    acao = escolha()
    comando = "DEFAULT"
    funcao = "Define um valor padrão para uma coluna quando nenhum valor é fornecido no INSERT"
    sintaxe = """
CREATE TABLE tabela (
    coluna tipo DEFAULT valor_padrao
);

Exemplo 1:
    CREATE TABLE clientes (
        id INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        data_cadastro DATE DEFAULT CURRENT_DATE,
        ativo BOOL DEFAULT TRUE,
        plano VARCHAR(20) DEFAULT 'Básico'
    );

Exemplo 2:
    CREATE TABLE produtos (
        id INT PRIMARY KEY,
        nome VARCHAR(200) NOT NULL,
        preco DECIMAL(10,2) DEFAULT 0.00,
        estoque INT DEFAULT 0,
        disponivel BOOL DEFAULT TRUE
    );

Exemplo 3:
    ALTER TABLE clientes
    ALTER COLUMN plano SET DEFAULT 'Básico';

    -- Inserindo (não precisa passar os campos com DEFAULT)
    INSERT INTO clientes (id, nome) 
    VALUES (1, 'João Silva');
    -- data_cadastro vai ser hoje, ativo = TRUE, plano = 'Básico'    
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def check():
    acao = escolha()
    comando = "CHECK"
    funcao = "Valida se os valores atendem a uma condição específica antes de serem inseridos ou atualizados"
    sintaxe = """
-- Na criação da tabela
CREATE TABLE tabela (
    coluna tipo CHECK (condição)
);

-- Ou como restrição separada
CREATE TABLE tabela (
    coluna tipo,
    CONSTRAINT nome_restricao CHECK (condição)
);

Exemplo 1 validando idade e salário: 
    CREATE TABLE funcionarios (
        id INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT CHECK (idade >= 18),
        salario DECIMAL(10,2) CHECK (salario > 0),
        data_admissao DATE
    );

Exemplo 2 com Múltiplas condições:
    CREATE TABLE produtos (
        id INT PRIMARY KEY,
        nome VARCHAR(200) NOT NULL,
        preco DECIMAL(10,2) CHECK (preco >= 0),
        estoque INT CHECK (estoque >= 0),
        categoria VARCHAR(50),
        CONSTRAINT check_categoria_valida CHECK (categoria IN ('Eletrônicos', 'Roupas', 'Alimentos', 'Livros'))
    );

Exemplo 3 com Check com data:
    CREATE TABLE pedidos (
        id INT PRIMARY KEY,
        data_pedido DATE DEFAULT CURRENT_DATE,
        data_entrega DATE,
        valor DECIMAL(10,2) CHECK (valor > 0),
        CHECK (data_entrega >= data_pedido)  -- Entrega não pode ser antes do pedido
    );

Exemplo 4 com Check completo:
    CREATE TABLE contas (
        id INT PRIMARY KEY,
        tipo VARCHAR(20),
        saldo DECIMAL(10,2),
        limite_credito DECIMAL(10,2),
        CHECK (
            (tipo = 'Corrente' AND saldo >= -limite_credito) OR
            (tipo = 'Poupança' AND saldo >= 0)
        )
    );
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"

def create_index():
    acao = escolha()       
    comando = "CREATE INDEX"
    funcao = "Cria uma estrutura de índice para acelerar buscas em colunas específicas, melhorando a performance de consultas"
    sintaxe = """
-- Índice simples em uma coluna
CREATE INDEX nome_indice
ON tabela (coluna);

-- Índice único (não permite valores duplicados)
CREATE UNIQUE INDEX nome_indice
ON tabela (coluna);

-- Índice composto (múltiplas colunas)
CREATE INDEX nome_indice
ON tabela (coluna1, coluna2);

Exemplo 1:
    CREATE INDEX idx_email
    ON clientes (email);

Exemplo 2:
    CREATE INDEX idx_nome_completo
    ON funcionarios (sobrenome, nome);

Exemplo 3:
    CREATE UNIQUE INDEX idx_cpf
    ON clientes (cpf);

Exemplo 4:
    CREATE INDEX idx_data_pedido
    ON pedidos (data_pedido);
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida" 
    
def drop_index():
    acao = escolha()       
    
    comando = "DROP INDEX"
    funcao = "Remove um índice existente do banco de dados"
    sintaxe = """
MySQL / MariaDB
    DROP INDEX nome_indice ON tabela;

PostgreSQL / SQL Server
    DROP INDEX nome_indice;

Oracle
    DROP INDEX nome_indice;
    
Exemplo 1:
    DROP INDEX idx_email ON clientes;

Exemplo 2: 
    DROP INDEX idx_nome_completo ON funcionarios;

Exemplo 3:
    DROP INDEX idx_cpf ON clientes;
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida" 
    
def create_view():
    acao = escolha()       
    
    comando = "CREATE VIEW"
    funcao = """
Cria uma visão (tabela virtual) baseada no resultado de uma consulta SELECT, permitindo reutilizar consultas complexas
"""
    sintaxe = """
CREATE VIEW nome_view AS
SELECT colunas
FROM tabelas
WHERE condicoes;

Exemplo 1 com View simples: 
    CREATE VIEW vw_clientes_ativos AS
    SELECT id, nome, email, telefone
    FROM clientes
    WHERE ativo = TRUE;

    -- Usando a view
    SELECT * FROM vw_clientes_ativos;

Exemplo 2 com View com dados resumidos:
    CREATE VIEW vw_resumo_vendas AS
    SELECT 
        p.categoria,
        COUNT(*) AS total_produtos,
        AVG(p.preco) AS preco_medio,
        SUM(p.estoque) AS estoque_total
    FROM produtos p
    GROUP BY p.categoria;

Exemplo 3 com  View com JOIN:
    CREATE VIEW vw_pedidos_detalhados AS
    SELECT 
        c.nome AS cliente_nome,
        c.email,
        p.id AS pedido_id,
        p.data_pedido,
        p.valor_total
    FROM clientes c
    INNER JOIN pedidos p ON c.id = p.cliente_id;
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida" 
    
def drop_view():
    acao = escolha()       
    
    comando = "DROP VIEW"
    funcao = "Remove uma view existente do banco de dados"
    sintaxe = """
DROP VIEW nome_view;

Exemplo 1: 
    DROP VIEW vw_clientes_ativos;

Exemplo 2:
    DROP VIEW vw_resumo_vendas;

Exemplo 3:
    DROP VIEW IF EXISTS vw_pedidos_detalhados;
"""
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"     

def case():
    acao = escolha()
    
    comando = "CASE"
    funcao = "Cria lógica condicional no SQL, permitindo retornar valores diferentes baseado em condições (como um IF/ELSE)"
    sintaxe = """
CASE SIMPLES:
    CASE expressão
        WHEN valor1 THEN resultado1
        WHEN valor2 THEN resultado2
        WHEN valorN THEN resultadoN
        ELSE resultado_padrão
    END

Exemplo:
    SELECT 
    nome,
    status,
    CASE status
        WHEN 'A' THEN 'Ativo'
        WHEN 'I' THEN 'Inativo'
        WHEN 'P' THEN 'Pendente'
        ELSE 'Desconhecido'
    END AS status_descricao
FROM clientes;

CASE BUSCADO:
    CASE 
        WHEN condição1 THEN resultado1
        WHEN condição2 THEN resultado2
        WHEN condiçãoN THEN resultadoN
        ELSE resultado_padrão
    END

Exemplo:
    SELECT 
        nome,
        nota,
        CASE 
            WHEN nota >= 7 THEN 'Aprovado'
            WHEN nota >= 5 THEN 'Recuperação'
            ELSE 'Reprovado'
        END AS situacao
    FROM alunos;
"""
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida" 
    
def begin_start():
    acao = escolha()
    
    comando = "BEGIN / START TRANSACTION"
    funcao = "Inicia uma transação, permitindo que múltiplos comandos sejam executados como uma única unidade atômica"
    sintaxe = """
BEGIN;
-- ou
START TRANSACTION;

Exemplo:
    BEGIN;  -- Começa a transação

    INSERT INTO clientes (id, nome, email) VALUES (1, 'João', 'joao@email.com');
    UPDATE contador SET total = total + 1;
    INSERT INTO log (acao, data) VALUES ('Cliente adicionado', NOW());

    -- Nada foi salvo permanentemente ainda
"""
 
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"  

def commit():
    acao = escolha()
    
    comando = "COMMIT"
    funcao = "Confirma permanentemente todas as alterações feitas desde o início da transação"
    sintaxe = """
COMMIT;

Exemplo:
    BEGIN;

    INSERT INTO pedidos (id, cliente_id, valor) VALUES (100, 1, 500.00);
    UPDATE clientes SET total_compras = total_compras + 500 WHERE id = 1;

    COMMIT;  -- Agora os dados estão salvos permanentemente
    """
    
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def rollback():
    acao = escolha()
    
    comando = "ROLLBACK"
    funcao = "Desfaz todas as alterações feitas desde o início da transação ou desde um SAVEPOINT"
    sintaxe = """
ROLLBACK;
-- ou
ROLLBACK TO SAVEPOINT nome_savepoint;

Exemplo:
    BEGIN;

    INSERT INTO produtos (id, nome, preco) VALUES (10, 'Notebook', 2500);
    INSERT INTO produtos (id, nome, preco) VALUES (11, 'Mouse', 50);

    ROLLBACK;  -- Nenhum produto foi inserido, tudo desfeito

    -- Tabela produtos continua como estava antes
"""
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
 
def savepoint():
    acao = escolha()
    
    comando = "SAVEPOINT"
    funcao = """
Cria um ponto de salvamento intermediário dentro de uma transação, permitindo desfazer apenas parte dela
"""
    sintaxe = """
SAVEPOINT nome_savepoint;
ROLLBACK TO SAVEPOINT nome_savepoint;

Exemplo:
    BEGIN;

    INSERT INTO clientes (id, nome) VALUES (1, 'João');
    SAVEPOINT cliente_adicionado;

    INSERT INTO pedidos (id, cliente_id, valor) VALUES (100, 1, 300);
    -- Ops, erro no pedido!
    ROLLBACK TO SAVEPOINT cliente_adicionado;  -- Desfaz só o pedido, mantém o cliente

    INSERT INTO pedidos (id, cliente_id, valor) VALUES (101, 1, 150);  -- Novo pedido correto

    COMMIT;  -- Salva cliente + pedido correto
"""
    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def union():
    acao = escolha()
    
    comando = "UNION"
    funcao = "Combina resultados de duas ou mais consultas, eliminando linhas duplicadas"
    sintaxe = """
SELECT colunas FROM tabela1
UNION
SELECT colunas FROM tabela2;

Exemplo 1 listando todos os clientes e fornecedores:
    SELECT nome, email, 'Cliente' AS tipo FROM clientes
    UNION
    SELECT nome, email, 'Fornecedor' AS tipo FROM fornecedores
    ORDER BY nome;

Exemplo 2 cidades com clientes OU fornecedores:
    SELECT cidade FROM clientes
    UNION
    SELECT cidade FROM fornecedores;

Exemplo 3 Produtos com estoque baixo OU pedidos pendentes:
    SELECT id, nome, 'Estoque Baixo' AS motivo FROM produtos WHERE estoque < 5
    UNION
    SELECT p.id, p.nome, 'Pedido Pendente' AS motivo
    FROM produtos p
    JOIN pedidos pe ON p.id = pe.produto_id
    WHERE pe.status = 'Pendente';
"""

    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def union_all():
    acao = escolha()
    comando = "UNION ALL"
    funcao = "Combina resultados de duas ou mais consultas, MANTENDO todas as linhas (inclusive duplicatas)"
    sintaxe = """
SELECT colunas FROM tabela1
UNION ALL
SELECT colunas FROM tabela2;

Exemplo 1 Listar TODOS os emails (com duplicatas):
    SELECT email FROM clientes
    UNION ALL
    SELECT email FROM fornecedores;

Exemplo 2 Relatório completo de movimentações: 
    SELECT data, valor, 'Venda' AS tipo FROM vendas
    UNION ALL
    SELECT data, valor, 'Compra' AS tipo FROM compras
    UNION ALL
    SELECT data, valor, 'Devolução' AS tipo FROM devolucoes
    ORDER BY data;

Exemplo 3 Log de atividades (manter todas as entradas):
    SELECT usuario, acao, data FROM log_sistema
    UNION ALL
    SELECT usuario, acao, data FROM log_backup
    ORDER BY data DESC
    LIMIT 100;    
"""

    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"
    
def intersect():
    acao = escolha()
    comando = "INTERSECT"
    funcao = "Retorna apenas as linhas que existem em AMBAS as consultas (interseção)"
    sintaxe = """
SELECT colunas FROM tabela1
INTERSECT
SELECT colunas FROM tabela2;

Exemplo 1 Clientes que também são fornecedores:
    SELECT nome, email FROM clientes
    INTERSECT
    SELECT nome, email FROM fornecedores;

Exemplo 2 Produtos em pedidos E em promoção:
    SELECT produto_id FROM pedidos
    INTERSECT
    SELECT produto_id FROM promocoes;

Exemplo 3 Cidades com clientes E fornecedores:
    SELECT cidade FROM clientes
    INTERSECT
    SELECT cidade FROM fornecedores;    
"""

    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"

def execpt():
    acao = escolha()

    comando = "EXCEPT / MINUS"
    funcao = "Retorna linhas da primeira consulta que NÃO existem na segunda consulta (diferença)"
    sintaxe = """
SELECT colunas FROM tabela1
EXCEPT
SELECT colunas FROM tabela2;

Exemplo 1 Clientes que NÃO são fornecedores:
    SELECT nome, email FROM clientes
    EXCEPT
    SELECT nome, email FROM fornecedores;

Exemplo 2 Produtos que nunca foram vendidos:
    SELECT id, nome FROM produtos
    EXCEPT
    SELECT DISTINCT produto_id, nome FROM itens_venda;

Exemplo 3 Funcionários que NÃO são clientes:
    SELECT cpf, nome FROM funcionarios
    EXCEPT
    SELECT cpf, nome FROM clientes;
"""

    if acao == "1":
        return comando
    elif acao == "2":
        return funcao
    elif acao == "3":
        return sintaxe
    else:
        return "Escolha inválida"

def criacao():
    valor = False
    tabela = []
    fk_list = []  # Lista para guardar as FKs
    soma = 0
    print("\nVamos criar sua tabela :)\n")
    nome_tabela = input("Qual o nome da sua tabela: ")
    loop = int(input("\nQuantos atributos vai ter: "))
    
    # Pergunta sobre chaves estrangeiras
    qtd_fk = int(input("\nQuantas chaves estrangeiras (FK) vai ter: "))
    
    for i in range(loop):
        atriutos = []
        nome_atributo = input(f"\nNome do {i+1}º atributo: ")
        tipo = int(input("""
O atributo é de qual tipo: 

1 - Texto
2 - Numérico
3 - Data/hora
4 - Booleano
5 - Binário:

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
    
def obs():
    resposta = """
Observação Importante:
    Este guia cobre aproximadamente 95% dos comandos SQL utilizados 
    no dia a dia de desenvolvimento, incluindo consultas, manipulação 
    de dados, estrutura de tabelas, joins, agrupamentos, subconsultas 
    e constraints
    
Este software não mostra os recursos avançados como:
    - Window Functions
    - Stored Procedures e Functions
    - Triggers
    - CTEs (Common Table Expressions)
    - MERGE (UPSERT)
    - Dynamic SQL
    - Comandos DCL (GRANT/REVOKE)
    - Recursos específicos de cada SGBD

Para ver essas funções avançadas, consulte documentações oficiais do banco de dados específico
"""
    return resposta

def agradecimentos():
    obrigados = """
Alura - Obrigado pelos cursos e pelo PDF da GLOSSÁRIO
GLOSSÁRIO - Obrigado pela ajuda para achar os comandos básicos de SQL    
Chat GPT - Obrigado pela ajuda da formação do modelo conceitual do Software e na listagem dos comandos de SQL    
Deep Seek - Obrigado pela ajuda na análise da lógica do código e a achar todos os erros de português 
Gemini - Obrigado pela ajuda na análise da lógica do código e por ter tirado dúvidas sobre certos comandos
"""
    return obrigados

# Software  
os.system("cls" if os.name == "nt" else "clear")
time.sleep(0.2)
while True:
    try:
        pulo = False
        print("""
Qual número você vai escolher:

+----------------------------+   +----------------------------+   +--------------------------+   +--------------------------+
|      DQL / DML / DDL       |   |   Estruturas e Conceitos   |   |   Agrupamento e Extras   |   |    Estruturas Finais     |
+----------------------------+   +----------------------------+   +--------------------------+   +--------------------------+
| 1  - SELECT                |   | 12 - ALTER TABLE           |   | 23 - HAVING              |   | 34 - CREATE VIEW         |
| 2  - WHERE                 |   | 13 - DROP TABLE            |   | 24 - Subconsultas Correl |   | 35 - DROP VIEW           |
| 3  - DISTINCT              |   | 14 - PRIMARY KEY           |   | 25 - LIMIT               |   | 36 - CASE                |
| 4  - ORDER BY              |   | 15 - FOREIGN KEY           |   | 26 - OFFSET              |   | 37 - BEGIN / START       |
| 5  - AS (ALIAS)            |   | 16 - Operadores Comparação |   | 27 - LIMIT + OFFSET      |   | 38 - COMMIT              |
| 6  - FROM                  |   | 17 - Operadores Lógicos    |   | 28 - NOT NULL            |   | 39 - ROLLBACK            |
| 7  - INSERT INTO           |   | 18 - Tipos                 |   | 29 - UNIQUE              |   | 40 - SAVEPOINT           |
| 8  - INSERT INTO + SELECT  |   | 19 - Agregações            |   | 30 - DEFAULT             |   | 41 - UNION               |
| 9  - UPDATE                |   | 20 - Subconjuntos          |   | 31 - CHECK               |   | 42 - UNION ALL           |
| 10 - DELETE                |   | 21 - JOIN                  |   | 32 - CREATE INDEX        |   | 43 - INTERSECT           |
| 11 - CREATE TABLE          |   | 22 - GROUP BY              |   | 33 - DROP INDEX          |   | 44 - EXCEPT              |
+----------------------------+   +----------------------------+   +--------------------------+   +--------------------------+

+--------------------------------------+   +--------------------------------------+
|           Comandos interativos       |   |            Comandos úteis            |
+--------------------------------------+   +--------------------------------------+
| 45 - Para criar uma tabela com ajuda |   | 46 - Para ver as observações         | 
+--------------------------------------+   | 47 - Para ver os Agradecimentos      |
                                           | 48 - Para sair                       |   
                                           +--------------------------------------+

Obs.: Lembre-se de quatro coisas:
    1 - Ao fazer um Banco de Dados em SQL o ; é muito importante para tudo funcionar, não esqueça dele
    2 - No uso do SQL quando for usar tabela.coluna, lembre que primeiro vem a TABELA, depois a COLUNA
    3 - O * é um Operador_Coringa / Wildcard que representa TUDO ou TODOS OS ELEMENTOS em determinado contexto
    4 - É importante usar a sintaxe tabela.coluna para evitar ambiguidades na consulta
    
    :)
""")

        opcao = input("Qual número vai ser: ")
        opcao = opcao.strip().lower()

        os.system("cls" if os.name == "nt" else "clear")
        if opcao == "1":
            resultado = select()
        elif opcao == "2":
            resultado = where()
        elif opcao == "3":
            resultado = distinct()
        elif opcao == "4":
            resultado = order_by()
        elif opcao == "5":
            resultado = alias()
        elif opcao == "6":
            resultado = fron()
        elif opcao == "7":
            resultado = insert_into()
        elif opcao == "8":
            resultado = insert_into_select()
        elif opcao == "9":
            resultado = update()
        elif opcao == "10":
            resultado = delete()
        elif opcao == "11":
            resultado = create_table()
        elif opcao == "12":
            resultado = alter_table()
        elif opcao == "13":
            resultado = drop_table()
        elif opcao == "14":
            resultado = pk()
        elif opcao == "15":
            resultado = fk()
        elif opcao == "16":
            resultado = operadores_de_comparacao()
        elif opcao == "17":
            resultado = operadores_logicos()
        elif opcao == "18":
            resultado = tipos()
        elif opcao == "19":
            resultado = agregacoes()
        elif opcao == "20":
            resultado = subconjuntos()
        elif opcao == "21":
            resultado = join()
        elif opcao == "22":
            resultado = group_by()
        elif opcao == "23":
            resultado = having()
        elif opcao == "24":
            resultado = sub_correla()
        elif opcao == "25":
            resultado = limit()
        elif opcao == "26":
            resultado = offset()
        elif opcao == "27":
            resultado = limit_and_offset()
        elif opcao == "28":
            resultado = not_null()
        elif opcao == "29":
            resultado = unique()
        elif opcao == "30":
            resultado = default()
        elif opcao == "31":
            resultado = check()
        elif opcao == "32":
            resultado = create_index()
        elif opcao == "33":
            resultado = drop_index()
        elif opcao == "34":
            resultado = create_view()
        elif opcao == "35":
            resultado = drop_view()
        elif opcao == "36":
            resultado = case()
        elif opcao == "37":
            resultado = begin_start()
        elif opcao == "38":
            resultado = commit()
        elif opcao == "39":
            resultado = rollback()
        elif opcao == "40":
            resultado = savepoint()
        elif opcao == "41":
            resultado = union()
        elif opcao == "42":
            resultado = union_all()
        elif opcao == "43":
            resultado = intersect()
        elif opcao == "44":
            resultado = execpt()
        elif opcao == "45":
            resultado = criacao()
        elif opcao == "46":
            resultado = obs()
        elif opcao == "0":
            os.system("cls" if os.name == "nt" else "clear")
            resultado = ""
            pulo = True
            time.sleep(0.2)
        elif opcao == "47":
            resultado = agradecimentos()
        elif opcao == "48":
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
            input("Dê enter para voltar ao início\n\n")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            continue
    except:
        break
