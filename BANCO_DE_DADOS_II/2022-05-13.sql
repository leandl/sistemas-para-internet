SELECT COUNT(cod_filme) FROM filmes WHERE titulo_original LIKE "%live%";


SELECT
  G.nome_genero,
  COUNT(cod_filme) as "Quantidade de Filmes",
  SUM(COALESCE(duracao, 0))/60 as "Quantidade de Horas"
FROM filmes F
RIGHT JOIN generos G on G.cod_genero = F.cod_genero
GROUP BY G.cod_genero
ORDER BY G.cod_genero;


SELECT D.nome_diretor, COUNT(F.cod_filme) AS total
FROM filmes F
INNER JOIN diretores D ON D.cod_diretor = F.cod_diretor
GROUP BY D.cod_diretor
HAVING total > 1
ORDER BY total DESC;


SELECT F.titulo, COUNT(E.cod_filme) as atores
FROM filmes F
INNER JOIN elenco E ON E.cod_filme = F.cod_filme
GROUP BY E.cod_filme
HAVING atores > 2
ORDER BY F.titulo ASC;
