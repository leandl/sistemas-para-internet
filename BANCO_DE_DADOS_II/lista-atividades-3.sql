-- 1. Exibir quantos filmes possui o banco de dados;
-- 159
SELECT COUNT(cod_filme) FROM filmes;


-- 2. Exibir quantos filmes com diretor possui o banco de dados;
-- 141
SELECT COUNT(cod_diretor) FROM filmes;


-- 3. Exibir quantos gêneros possuem algum filme vinculado existem no banco de dados;
-- 14
SELECT COUNT(DISTINCT cod_genero) FROM filmes;

-- 4. Exibir quantos gêneros não possuem algum filme vinculado existem no banco de dados;
-- 3
SELECT COUNT(G.cod_genero)
FROM filmes F
RIGHT JOIN generos G ON F.cod_genero = G.cod_genero
WHERE F.cod_genero IS NULL;

-- 5. Exibir quantas horas eu preciso para assistir todos filmes;
-- aproximadamente 313 horas
SELECT SUM(duracao)/60 FROM filmes;

-- 6. Exibir quantas horas eu preciso para assistir todos os filmes de suspense;
-- aproximadamente 12,5 horas
SELECT SUM(F.duracao)/60
FROM filmes F
INNER JOIN generos G ON F.cod_genero = G.cod_genero
WHERE G.nome_genero = "Suspense";

-- 7. Exibir quantas horas eu preciso para assistir todos os filmes que Johnny Depp e Orlando
-- Bloom atuaram juntos.
-- Aproximadamente 7 horas
SELECT SUM(F.duracao)/60
FROM filmes F
INNER JOIN elenco E ON E.cod_filme = F.cod_filme
INNER JOIN atores A ON A.cod_ator = E.cod_ator
WHERE
  A.nome_ator = "Johnny Depp" AND
  E.cod_filme IN (
    SELECT E.cod_filme
    FROM elenco E
    INNER JOIN atores A ON A.cod_ator = E.cod_ator
    WHERE A.nome_ator = "Orlando Bloom"
  );

-- 8. Listar o nome dos atores e a quantidade de filmes daqueles que atuam em cinco ou mais
-- filmes em ordem alfabética (usar junção interna).
-- 15 linhas X 2 colunas – começando com [Bruce Willis |5] e terminando com [Tom Cruise |7]
SELECT A.nome_ator, COUNT(E.cod_filme) as quantidade_filmes
FROM elenco E
INNER JOIN atores A ON A.cod_ator = E.cod_ator
GROUP BY A.nome_ator
HAVING quantidade_filmes > 4
ORDER BY A.nome_ator ASC;


-- 9. Listar o nome_genero e o número de filmes para cada gênero existente no banco de
-- dados (lembre-se que podem existir gêneros para os quais não existem filmes
-- cadastrados).
-- 17 linhas X 2 colunas – começando com [Ação |30] e terminando com [Suspense |7]
SELECT G.nome_genero, COUNT(F.cod_filme)
FROM filmes F
RIGHT JOIN generos G ON G.cod_genero = F.cod_genero
GROUP BY G.nome_genero;



-- 10. Listar o nome_genero e a respectiva duração total (soma das durações dos filmes) dos
-- gêneros que possuem 20 ou mais filmes.
SELECT G.nome_genero, SUM(F.duracao)
FROM filmes F
INNER JOIN generos G ON G.cod_genero = F.cod_genero
GROUP BY G.nome_genero
HAVING COUNT(*) > 19;


-- 11. Listar o nome dos diretores e a quantidade de filmes que cada um fez ordenados
-- alfabeticamente (lembre-se que podem existir diretores que ainda não dirigiram nenhum
-- filme cadastrado).
-- 112 linhas X 2 colunas – começando com Adam Shankman |1
SELECT D.nome_diretor, COUNT(F.cod_filme)
FROM filmes F
RIGHT JOIN diretores D ON D.cod_diretor = F.cod_diretor
GROUP BY D.cod_diretor
ORDER BY D.nome_diretor;



-- 12. Listar o nome dos diretores, que dirigiram mais que um filme, ordenados
-- alfabeticamente.
-- 24 linhas X 2 colunas – começando com John Woo | 2
SELECT D.nome_diretor, COUNT(F.cod_filme) as total
FROM filmes F
RIGHT JOIN diretores D ON D.cod_diretor = F.cod_diretor
GROUP BY D.cod_diretor
HAVING total > 1
ORDER BY D.nome_diretor;


-- 13. Mostrar o nome do gênero e a quantidade de filmes do gênero que possui mais filmes.
-- 1 linha X 2 colunas – Ação | 30
SELECT G.nome_genero, COUNT(F.cod_filme)
FROM filmes F
INNER JOIN generos G ON G.cod_genero = F.cod_genero
GROUP BY G.nome_genero
LIMIT 1;


-- 14. Exibir o título e a duração do filme que possui a maior duração, sem usar as cláusulas
-- LIMIT e ORDER. Dica: utilize subconsulta.
-- 1 linha X 2 colunas – Friends - 3ª Temporada | 589
SELECT titulo, duracao FROM filmes
WHERE duracao IN (SELECT MAX(duracao) FROM filmes);


-- 15. Exibir o nome_diretor e a quantidade de filmes do diretor que mais dirigiu filmes e do
-- diretor que menos dirigiu filmes. Existem alguns empates pois vários diretores dirigiram
-- somente um filme. Portanto, o resultado pode ser diferente na segunda linha.
SELECT D.nome_diretor, COUNT(F.cod_filme) as total
FROM filmes F
RIGHT JOIN diretores D ON D.cod_diretor = F.cod_diretor
GROUP BY D.cod_diretor
HAVING 
  total IN (
    SELECT MAX(table_qtd_max.qtd_filmes)
    FROM (
      SELECT COUNT(F.cod_filme) as qtd_filmes
      FROM filmes F
      RIGHT JOIN diretores D ON D.cod_diretor = F.cod_diretor
      GROUP BY D.cod_diretor
    ) table_qtd_max
  )
  OR 
  total IN (
    SELECT MIN(table_qtd_min.qtd_filmes)
    FROM (
      SELECT COUNT(F.cod_filme) as qtd_filmes
      FROM filmes F
      RIGHT JOIN diretores D ON D.cod_diretor = F.cod_diretor
      GROUP BY D.cod_diretor
    ) table_qtd_min
  )
ORDER BY total DESC;



-- 16. Exibir o titulo de todos os filmes e a respectiva quantidade de atores, ordenados pela
-- quantidade, começando pelo que tem mais atores (lembre-se que podem existir filmes
-- que não possuem atores).
-- 158 linhas – começando com Top Gun - Ases Indomáveis | 5
SELECT F.titulo, COUNT(A.cod_ator) as atores
FROM filmes F
LEFT JOIN elenco E ON E.cod_filme = F.cod_filme
INNER JOIN atores A ON A.cod_ator = E.cod_ator
GROUP BY F.cod_filme
ORDER BY atores DESC;

-- 17. Exibir o nome_genero, a quantidade de filmes e, na terceira coluna, o título dos filmes do
-- respectivo gênero, separados por “;” (ponto e vírgula), dos gêneros com menos de 6
-- filmes mas que contenham ao menos um filme.
SELECT
  G.nome_genero,
  COUNT(F.cod_filme),
  GROUP_CONCAT(DISTINCT F.titulo ORDER BY F.titulo SEPARATOR ", ")
FROM filmes F
RIGHT JOIN generos G ON G.cod_genero = F.cod_genero
GROUP BY G.nome_genero;
