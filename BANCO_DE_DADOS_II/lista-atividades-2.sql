use filmes;

-- 1. Listar o título dos filmes e seu respectivo gênero, incluindo na lista os gêneros que não
-- possuem filmes.
SELECT F.titulo, G.nome_genero
FROM filmes F
RIGHT JOIN generos G ON F.cod_genero = G.cod_genero;


-- 2. Listar o nome dos atores que atuam nos 5 filmes de maior duração (Dica: usar relações
-- derivadas, order e limit).
SELECT F.titulo, F.duracao, A.nome_ator
FROM (SELECT cod_filme, titulo, duracao FROM filmes ORDER BY duracao DESC LIMIT 5) as F 
INNER JOIN elenco E ON E.cod_filme = F.cod_filme
INNER JOIN atores A ON E.cod_ator = A.cod_ator
ORDER BY F.duracao DESC;


-- 3. Listar o nome dos atores, em ordem alfabética, que nunca gravaram um filme.
SELECT A.nome_ator
FROM atores A
LEFT JOIN elenco E ON A.cod_ator = E.cod_ator
WHERE E.cod_filme IS NULL; 


-- 4. Listar o título em português dos filmes que sejam dos seguintes gêneros: Infantil,
-- Aventura ou Show (usar consultas aninhadas e a cláusula IN).
SELECT F.titulo, G.nome_genero
FROM filmes F
INNER JOIN generos G ON F.cod_genero = G.cod_genero
WHERE G.nome_genero IN ("Infantil", "Aventura", "Show");


-- 5. Listar o título em português dos filmes dos gêneros: Ação, Infantil e Comédia, lançados
-- após 2005 (usar junção interna e a cláusula IN).
SELECT F.titulo, G.nome_genero, F.ano_lancamento
FROM filmes F
INNER JOIN generos G ON F.cod_genero = G.cod_genero
WHERE 
  G.nome_genero IN ("Ação", "Infantil", "Comédia") AND
  F.ano_lancamento > "2006";


-- 6. Quais diretores não fizeram nenhum filme? Faça este comando SQL sem utilizar a palavra
-- NULL em todo código.
SELECT D.nome_diretor
FROM diretores D
WHERE 
  D.cod_diretor NOT IN (
    SELECT F.cod_diretor
    FROM filmes F
    WHERE F.cod_diretor > 0
  );

SELECT D.nome_diretor
FROM filmes F
RIGHT JOIN diretores D on F.cod_diretor = D.cod_diretor
WHERE F.cod_filme IS NULL;

-- 7. Exibir a lista de filmes que não possui nenhum ator (elenco).
SELECT F.titulo 
FROM filmes F
LEFT JOIN elenco E ON F.cod_filme = E.cod_filme
WHERE E.cod_filme IS NULL; 