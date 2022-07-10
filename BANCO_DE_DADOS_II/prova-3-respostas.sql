-- Visões
-- 1 ) Implemente uma VIEW que exiba o nome, valor e nome da
-- categoria dos imóveis que estão para aluguel em Imbituba

CREATE VIEW imoveis_em_imbituba AS
SELECT I.nome, I.valor, C.nome as categoria
FROM imovel I
INNER JOIN categoria C ON C.id = I.categoria_id
INNER JOIN municipio M ON M.id = I.municipio_id
WHERE M.nome = "Imbituba";

SELECT * FROM imoveis_em_imbituba;