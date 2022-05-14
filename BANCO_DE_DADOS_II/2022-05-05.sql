SELECT SUM(duracao)/60
FROM filmes
WHERE duracao != 0;

SELECT AVG(duracao) as media FROM filmes;
SELECT STDDEV_POP(duracao) as media FROM filmes;

SELECT COUNT(cod_filme) - COUNT(cod_diretor) FROM filmes;

SELECT COUNT(DISTINCT ano_lancamento) FROM filmes;
SELECT COUNT(DISTINCT cod_genero)
FROM filmes;

SELECT COUNT(f.cod_filme)
FROM filmes f
INNER JOIN generos G ON f.cod_genero = G.cod_genero
WHERE G.nome_genero = "Drama";


SELECT SUM(F.duracao)/60
FROM filmes F
INNER JOIN elenco E ON F.cod_filme=E.cod_filme
INNER JOIN atores A ON E.cod_ator=A.cod_ator
WHERE A.nome_ator = "Brad Pitt";

SELECT COUNT(F.cod_filme)
FROM filmes F
INNER JOIN elenco E ON F.cod_filme=E.cod_filme
INNER JOIN atores A ON E.cod_ator=A.cod_ator
WHERE A.nome_ator = "Brad Pitt";


SELECT
  F.titulo,
  GROUP_CONCAT(DISTINCT A.nome_ator ORDER BY A.nome_ator SEPARATOR ", ")
FROM filmes F
INNER JOIN elenco E ON F.cod_filme=E.cod_filme
INNER JOIN atores A ON E.cod_ator=A.cod_ator
WHERE F.titulo LIKE "Friend%"
GROUP BY F.titulo;


SELECT ano_lancamento, AVG(duracao)
FROM filmes
GROUP BY ano_lancamento;

SELECT D.nome_diretor, COUNT(F.cod_filme)
FROM filmes F
RIGHT JOIN diretores D ON F.cod_diretor = D.cod_diretor
GROUP BY D.nome_diretor;

SELECT
  D.nome_diretor,
  COALESCE(
    GROUP_CONCAT(DISTINCT F.titulo ORDER BY F.titulo SEPARATOR ", "),
    "Sem registros"
  )
FROM filmes F
RIGHT JOIN diretores D ON F.cod_diretor = D.cod_diretor
GROUP BY D.nome_diretor;
