-- 1.1) Cadastro de novos pedidos (orders) e suas respectivas informações (orderdetails). Um
-- pedido pode ter múltiplos produtos em múltiplas quantidades; 
-- Sem Resposta.

-- 1.2) Pesquisa por palavras-chave nos comentários dos pedidos;
EXPLAIN SELECT * FROM orders WHERE comments LIKE '%Ferrari%'; 
-- select_type: SIMPLE
-- table: orders
-- type: ALL
-- possible_keys: null
-- key: null
-- key_len: null
-- ref: null
-- rows: 328
-- Extra: Using where

ALTER TABLE orders ADD FULLTEXT(comments);
EXPLAIN SELECT * FROM orders WHERE MATCH(comments) AGAINST('*Ferrari*');	
-- select_type: SIMPLE
-- table: orders
-- type: fulltext
-- possible_keys: comments
-- key: comments
-- key_len: 0
-- ref: 
-- rows: 1
-- Extra: Using where

-- 1.3) Quantidade pedida agrupada por produto – vide orderdetails;
EXPLAIN SELECT p.productName, SUM(od.quantityOrdered) FROM products p, orderdetails od WHERE p.productCode = od.productCode AND p.productName = '2003 Harley-Davidson Eagle Drag Bike';
-- select_type: SIMPLE
-- table: p
-- type: ALL
-- possible_keys: PRIMARY
-- key: null
-- key_len: null
-- ref: null
-- rows: 110
-- Extra: Using where

-- select_type: SIMPLE
-- table: od
-- type: ref
-- possible_keys: productCode
-- key: productCode
-- key_len: 17
-- ref: classicmodels2.p.productCode
-- rows: 13
-- Extra: 

ALTER TABLE products ADD FULLTEXT(productName);
EXPLAIN SELECT p.productName, SUM(od.quantityOrdered) FROM products p, orderdetails od WHERE p.productCode = od.productCode AND MATCH(p.productName) AGAINST('2003 Harley-Davidson Eagle Drag Bike');		
-- select_type: SIMPLE,
-- table: p,
-- type: fulltext,
-- possible_keys: PRIMARY,productName,
-- key: productName,
-- key_len: 0,
-- ref: ,
-- rows: 1,
-- Extra: Using where

-- select_type: SIMPLE,
-- table: od,
-- type: ref,
-- possible_keys: productCode,
-- key: productCode,
-- key_len: 17,
-- ref: classicmodels2.p.productCode,
-- rows: 13,
-- Extra: 

--- 1.4) Pesquisa pelo distribuidor de um produto (products.productVendor).
EXPLAIN SELECT * FROM products WHERE productVendor = 'Classic Metal Creations';
-- select_type: SIMPLE,
-- table: products,
-- type: ALL,
-- possible_keys: null,
-- key: null,
-- key_len: null,
-- ref: null,
-- rows: 110,
-- Extra: Using where

ALTER TABLE products ADD FULLTEXT(productVendor);
EXPLAIN SELECT * FROM products WHERE MATCH(productVendor) AGAINST('Classic Metal Creations');
-- select_type: SIMPLE
-- table: products
-- type: fulltext
-- possible_keys: productVendor
-- key: productVendor
-- key_len: 0
-- ref: 
-- rows: 1
-- Extra: Using where

-- 1.5) Pesquisa pelo ano do modelo de um produto (products.productName). Ex: “1957 Corvette
-- Convertible”.
-- Nesta questão, como já haviamos criado um INDEX no campo 'productName' para resolver o 
-- problema 3, não necessitamos criar mais nenhum novo index para melhora de pesquisa,
-- isso pois podemos adaptar o SELECT para procurar apenas o ano desejado.

EXPLAIN SELECT * FROM products WHERE MATCH(productName) AGAINST('+1957*')
-- "select_type": "SIMPLE",
-- "table": "products",
-- "type": "fulltext",
-- "possible_keys": "productName",
-- "key": "productName",
-- "key_len": "0",
-- "ref": "",
-- "rows": "1",
-- "Extra": "Using where"


-- 1.6) Lista dos escritórios – filiais (offices).
-- Não achamos necessário criar um index na tabela 'offices', isso porque ela possui pouco registros.
-- Mesmo no pior dos casos o número de liunhas pesquisadas não seria mais do que 7. 

-- 1.6) Lista de todos produtos ordenados pelo valor;
-- Não tem o que fazer.

##########################################################################

-- Ethan --
-- 2.1) Ethan é o encarregado em fazer backup 3 vezes por dia do banco de dados.
GRANT SELECT ON classicmodels.* TO 'ethan'@'localhost' IDENTIFIED BY 'senhaEthan';
GRANT FILE ON *.* TO 'ethan'@'localhost';
GRANT LOCK TABLES  ON classicmodels.* TO 'ethan'@'localhost';

-- Comando de backup
mysqldump -u ethan -p classicmodels < nome_do_arquivo.sql

-- Jhon --
-- 2.2) Jhon é o database administrator. Ele que deve poder propor e implementar novas estruturas, dar e
-- remover acessos a usuários e acessar todas informações.
GRANT ALL PRIVILEGES ON *.* TO 'jhon'@'localhost' IDENTIFIED BY '123' WITH GRANT OPTION;
REVOKE INSERT, DELETE, UPDATE ON *.* FROM 'jhon'@'localhost';

-- Kay --
-- 2.3) Kay utiliza um sistema exclusivo para o marketing. Através dele enviará recomendações de produtos
-- eventualmente para os clientes já cadastrados.
GRANT SELECT ON classicmodels.products TO 'kay'@'localhost' IDENTIFIED BY '123';
GRANT SELECT ON classicmodels.productlines TO 'kay'@'localhost';
GRANT SELECT ON classicmodels.customers TO 'kay'@'localhost';

-- WebSite --
-- 2.4) O website da empresa apenas consulta os produtos e os escritórios, exibindo em páginas
-- específicas. Ele também deve ter um usuário no BD específico.
GRANT SELECT ON classicmodels.products TO 'website'@'localhost' IDENTIFIED BY '123';
GRANT SELECT ON classicmodels.offices TO 'website'@'localhost';

-- Jennifer --
-- 2.5) Jennifer cuida da parte comercial e administrativa. Ela deve conseguir consultar, inserir e atualizar
-- qualquer informação no BD.
GRANT SELECT, INSERT, UPDATE ON classicmodels.* TO 'jennifer'@'localhost' IDENTIFIED BY '123';

-- Peter --
-- 2.6) Peter é o CEO. Ele possui acesso a todas informações do BD e é o único que pode apagar
-- informações. Ele não sabe projetar bancos então não deve ter acesso a comandos de SQL DDL.
GRANT ALL PRIVILEGES ON *.* TO 'peter'@'localhost' IDENTIFIED BY '123';
REVOKE CREATE, DELETE, DROP, ALTER, EVENT, INDEX, TRIGGER, ALTER ROUTINE, CREATE ROUTINE, CREATE TEMPORARY TABLES ON *.* FROM 'peter'@'localhost';
