
-- Create indexes for Query 1
CREATE INDEX product_price_idx ON product (price);
CREATE INDEX order_date_idx ON "order" (date);

-- Create an index for Query 2
CREATE INDEX product_name_idx ON product (name);


SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023

SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

-- Para optimizar os tempos de consulta para as consultas fornecidas, pode adicionar índices às colunas relevantes. Com base na natureza das operações e nas informações fornecidas, eis os índices recomendados para cada consulta:
--
--Para a Consulta 1:
--
--Justificação: A consulta filtra com base na coluna de preço e efectua uma comparação de intervalos na coluna de data.
--Tipo de índice: Índice de árvore B
--Atributos e tabelas:
--coluna preço na tabela produto
--coluna data na tabela "order
--sql
--Código de cópia
---- Criar índices para a Consulta 1
--CREATE INDEX product_price_idx ON product (price);
--CREATE INDEX order_date_idx ON "order" (date);
--Para a Consulta 2:
--
--Justificativa: A consulta filtra com base nos caracteres iniciais da coluna name e envolve agregação (SUM) no cálculo qty*price.
--Tipo de índice: Índice B-tree
--Atributos e tabelas:
--coluna nome na tabela produto
--sql
--Código de cópia
---- Criar um índice para a Consulta 2
--CREATE INDEX nome_do_produto_idx ON produto (nome);
--Esses índices ajudarão a acelerar a execução das consultas correspondentes, permitindo a recuperação eficiente de dados com base nas condições especificadas.
--
--Tenha em atenção que as recomendações de índices fornecidas assumem uma carga de trabalho e uma distribuição de dados típicas. É importante monitorizar e analisar o desempenho da consulta e ajustar os índices conforme necessário com base nas características específicas dos seus dados e padrões de carga de trabalho.
--
--Traduzido com a versão gratuita do tradutor - www.DeepL.com/Translator