-- QUESTAO 1
SELECT *
FROM empregados
WHERE
  nomeempr LIKE "%jose%" AND
  sexo="M" AND
  salario > 3000;


-- QUESTAO 2
SELECT D.nomedepto, E.nomeempr
FROM empregados E
INNER JOIN departamentos D ON D.matriculager = E.matricula;


-- QUESTAO 3
SELECT E.nomeempr, COUNT(D.nomedep)
FROM empregados E
LEFT JOIN dependentes D ON D.matricula = E.matricula
GROUP BY E.nomeempr;


-- QUESTAO 4
SELECT E.nomeempr
FROM empregados E
LEFT JOIN dependentes D ON D.matricula = E.matricula
GROUP BY E.nomeempr
HAVING COUNT(D.nomedep) = 0;

-- OU

SELECT E.nomeempr
FROM empregados E
LEFT JOIN dependentes D ON D.matricula = E.matricula
WHERE D.nomedep IS NULL;

-- QUESTAO 5
SELECT AVG(E.salario)
FROM empregados E
WHERE sexo="F";

-- QUESTAO 6
SELECT SUM(E.salario)
FROM empregados E
INNER JOIN trabalha_em T ON T.matricula = E.matricula
INNER JOIN projetos P ON P.numproj = T.numproj
WHERE P.nomeproj = "Zeus";

-- QUESTAO 7
SELECT SUM(SD.salario)
FROM (
  SELECT E.salario
  FROM empregados E
  LEFT JOIN dependentes D ON D.matricula = E.matricula
  GROUP BY E.nomeempr
  HAVING COUNT(D.nomedep) != 0
) as SD;

-- QUESTAO 8
SELECT E.nomeempr, E.salario
FROM empregados E
INNER JOIN trabalha_em T ON T.matricula = E.matricula
INNER JOIN projetos P ON P.numproj = T.numproj
WHERE
  P.nomeproj = "Medusa" AND
  T.horas > 25;

-- QUESTAO 9
SELECT P.nomeproj
FROM empregados E
INNER JOIN trabalha_em T ON T.matricula = E.matricula
INNER JOIN projetos P ON P.numproj = T.numproj
WHERE
  E.nomeempr = "Pedro Dantas" AND
  P.numproj IN (
    SELECT P.numproj
    FROM empregados E
    INNER JOIN trabalha_em T ON T.matricula = E.matricula
    INNER JOIN projetos P ON P.numproj = T.numproj
    WHERE E.nomeempr = "Paula de Queiroz"
  );


-- QUESTAO 10
SELECT DISTINCT E.nomeempr
FROM empregados E
INNER JOIN trabalha_em T ON T.matricula = E.matricula
INNER JOIN projetos P ON P.numproj = T.numproj
INNER JOIN departamentos D ON D.coddepto = P.coddepto
WHERE D.nomedepto = "Desenvolvimento de Software";
