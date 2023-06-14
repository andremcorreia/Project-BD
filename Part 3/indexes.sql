
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

-- Para optimizar os tempos de consulta para as consultas fornecidas, adicionámos indexes às colunas relevantes:
--
--Para a primeira Query:
--
-- A query filtra com base na coluna de preço e efectua uma comparação de intervalos na coluna de data.
--Tipo de índice: B+ Tree Index
--Atributos e tabelas:
--coluna price na tabela product
--coluna date na tabela "order"
---- Indíces:
--CREATE INDEX product_price_idx ON product (price);
--CREATE INDEX order_date_idx ON "order" (date);

--Para a segunda Query:
--
-- A query filtra com base nos caracteres iniciais da coluna name e envolve agregação (SUM) no cálculo qty*price.
--Tipo de índice: B+ Tree Index
--Atributos e tabelas:
--coluna name na tabela product
---- Indíces:
--CREATE INDEX product_name_idx ON product (name);



--Estes índices ajudarão a acelerar a execução das consultas correspondentes, permitindo a recuperação eficiente de dados com base nas condições especificadas.
