use filmes;

SHOW DATABASES;

/*1. Exibir os filmes que possuam a palavra “amor” ou “love” no título ou título original.*/
SELECT * 
FROM filmes 
WHERE 
  (titulo LIKE "%amor%" OR titulo LIKE "%love%") OR
  (titulo_original LIKE "%amor%" OR titulo_original LIKE "%love%");


/*2. Exibir os filmes cujo título é igual ao título original.*/
SELECT * FROM filmes WHERE titulo=titulo_original;


/*3. Exibir o título e a a duração do filme mais longo.*/
SELECT titulo, duracao FROM filmes ORDER BY duracao DESC LIMIT 1;


/*4. Exibir os filmes feitos pelo diretor Christopher Nolan.*/
SELECT 
  titulo
FROM 
  filmes F, diretores D 
WHERE
  F.cod_diretor = D.cod_diretor AND
  D.nome_diretor = "Christopher Nolan";

/*5. Exibir o título e o ano de lançamento dos 3 filmes mais recentes feitos pelo ator Brad Pitt.*/
SELECT 
  F.titulo, F.ano_lancamento
FROM 
  filmes F, elenco E, atores A
WHERE 
  F.cod_filme = E.cod_filme AND
  A.cod_ator = E.cod_ator AND
  A.nome_ator = "Brad Pitt"
ORDER BY F.ano_lancamento DESC
LIMIT 3;
  


/*6. Exibir filmes curtos, entre 60 e 80 minutos.*/
SELECT * FROM filmes WHERE duracao BETWEEN 60 AND 80;



/*7. Exibir os atores (sem repetição) de qualquer filme da série Harry Potter.*/
SELECT 
  DISTINCT(A.nome_ator)
FROM 
  filmes F, elenco E, atores A
WHERE 
  F.cod_filme = E.cod_filme AND
  A.cod_ator = E.cod_ator AND
  F.titulo LIKE "%Harry Potter%"
ORDER BY A.nome_ator;



/*8. Exibir os registros da tabela filmes que não contenham um diretor.*/
SELECT * FROM filmes WHERE cod_diretor IS NULL;



/*9. Exibir a lista de diretores (sem repetição) que dirigiram algum filme entre 1990 e 1995
(incluindo 1990 e 1995).*/
SELECT 
  DISTINCT(D.nome_diretor)
FROM 
  filmes F, diretores D 
WHERE
  F.cod_diretor = D.cod_diretor AND
  F.ano_lancamento BETWEEN 1990 AND 1995
ORDER BY D.nome_diretor;


/*10. Exibir os filmes de suspense feitos pelo ator Al Pacino.*/
SELECT 
  F.titulo, G.nome_genero, F.ano_lancamento
FROM 
  filmes F, elenco E, atores A, generos G
WHERE 
  F.cod_filme = E.cod_filme AND
  A.cod_ator = E.cod_ator AND
  A.nome_ator = "Al Pacino" AND
  F.cod_genero = G.cod_genero AND
  G.nome_genero = "Suspense"
ORDER BY F.ano_lancamento DESC;