-- Visões
-- 1 ) Implemente uma VIEW que exiba o nome, valor e nome da
-- categoria dos imóveis que estão para aluguel em Imbituba

CREATE VIEW imoveis_em_imbituba AS
SELECT I.nome, I.valor, C.nome as categoria
FROM imovel I
INNER JOIN categoria C ON C.id = I.categoria_id
INNER JOIN municipio M ON M.id = I.municipio_id
WHERE 
  M.nome = "Imbituba" AND
  I.finalidade = "aluguel";

SELECT * FROM imoveis_em_imbituba;

-- Procedimentos
-- 2 ) Implemente uma STORE PROCEDURE que recebe dois valores
-- (mínimo e máximo) e exiba os imóveis para venda nesta faixa.
-- OBS: A lista de imóveis a venda deve vir de uma view espec�fica de
-- imoveis sendo vendidos.

CREATE VIEW imoveis_a_venda AS
SELECT *
FROM imovel
WHERE finalidade = "venda";

DELIMITER $$
CREATE PROCEDURE imoveis_a_vendas_in_faixa(valor_min INT, valor_max INT)
   BEGIN
   SELECT * FROM imoveis_a_venda WHERE valor BETWEEN valor_min AND valor_max;
   END $$
DELIMITER ;

CALL imoveis_a_vendas_in_faixa(138000.00, 198000.00);

-- Gatilhos
-- 1) Implemente uma TRIGGER que faça backup em outra tabela dos imóveis que
-- forem excluídos.

CREATE TABLE `imovel_backup` (
    `id` int NOT NULL AUTO_INCREMENT,
    `nome` char(150) NOT NULL,
    `descricao` text,
    `data_cadastro` date DEFAULT NULL,
    `finalidade` char(10) DEFAULT NULL,
    `dormitorios` tinyint DEFAULT NULL,
    `area` int DEFAULT NULL,
    `valor` decimal(10, 2) DEFAULT NULL,
    `categoria_id` int DEFAULT NULL,
    `bairro_id` int DEFAULT NULL,
    `municipio_id` int NOT NULL,
    `proprietario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_imovel_backup_categoria` (`categoria_id`),
  KEY `FK_imovel_backup_cliente` (`proprietario_id`),
  KEY `FK_imovel_backup_municipio` (`municipio_id`),
  KEY `FK_imovel_backup_bairro` (`bairro_id`),
  CONSTRAINT `FK_imovel_backup_bairro` FOREIGN KEY (`bairro_id`) REFERENCES `bairro`(`id`) ON DELETE
  SET
    NULL ON
  UPDATE
  SET
    NULL,
    CONSTRAINT `FK_imovel_backup_categoria` FOREIGN KEY (`categoria_id`) REFERENCES `categoria`(`id`) ON DELETE CASCADE ON
  UPDATE
    CASCADE,
    CONSTRAINT `FK_imovel_backup_cliente` FOREIGN KEY (`proprietario_id`) REFERENCES `proprietario`(`id`) ON DELETE CASCADE ON
  UPDATE
    CASCADE,
    CONSTRAINT `FK_imovel_backup_municipio` FOREIGN KEY (`municipio_id`) REFERENCES `municipio`(`id`) ON
  UPDATE
    CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 20 DEFAULT CHARSET = latin1;


DELIMITER $$
CREATE TRIGGER backup_imoveis AFTER DELETE ON imovel
   FOR EACH ROW BEGIN
      INSERT INTO imovel_backup(id, nome, descricao, data_cadastro, finalidade, dormitorios, area, valor, categoria_id, bairro_id, municipio_id, proprietario_id)
      VALUES (OLD.id, OLD.nome, OLD.descricao, OLD.data_cadastro, OLD.finalidade, OLD.dormitorios, OLD.area, OLD.valor, OLD.categoria_id, OLD.bairro_id, OLD.municipio_id, OLD.proprietario_id);
   END $$
DELIMITER ;


-- 2) Modifique o BD de forma que cada proprietário tenha uma coluna com o valor
-- total de seu patrimônio. Cada vez que um imóvel é adicionado, alterado ou
-- excluído, o respectivo valor de patrimônio do proprietário deve ser atualizado.