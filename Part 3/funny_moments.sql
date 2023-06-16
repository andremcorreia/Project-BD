-- nada
EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;
---------------------------------------------------------------------------------
-- price
CREATE INDEX product_price_idx ON product (price);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS product_price_idx;

---------------------------------------------------------------------------------
-- date
CREATE INDEX order_date_idx ON "order" (date);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS order_date_idx;

-----------------------------------------------------------------------------------


-----------------------------------------------------------------------------------
-- name
CREATE INDEX product_name_idx ON product (name);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS product_name_idx;

-----------------------------------------------------------------------------------
-- price date
CREATE INDEX product_price_idx ON product (price);

CREATE INDEX order_date_idx ON "order" (date);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS product_price_idx;
DROP INDEX IF EXISTS order_date_idx;

-----------------------------------------------------------------------------------
-- price date sku
CREATE INDEX product_price_idx ON product (price);

CREATE INDEX order_date_idx ON "order" (date);

CREATE INDEX idx_contains_sku ON contains(SKU);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS product_price_idx;
DROP INDEX IF EXISTS order_date_idx;
DROP INDEX IF EXISTS idx_contains_sku;

-----------------------------------------------------------------------------------
-- sku name
CREATE INDEX idx_contains_sku ON contains(SKU);

CREATE INDEX product_name_idx ON product (name);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS idx_contains_sku;
DROP INDEX IF EXISTS product_name_idx;

-----------------------------------------------------------------------------------
-- date sku name
CREATE INDEX order_date_idx ON "order" (date);

CREATE INDEX idx_contains_sku ON contains(SKU);

CREATE INDEX product_name_idx ON product (name);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS idx_contains_sku;
DROP INDEX IF EXISTS product_name_idx;
DROP INDEX IF EXISTS order_date_idx;
-----------------------------------------------------------------------------------
-- price date sku name
CREATE INDEX product_name_idx ON product (name);

CREATE INDEX product_price_idx ON product (price);

CREATE INDEX order_date_idx ON "order" (date);

CREATE INDEX idx_contains_sku ON contains(SKU);

EXPLAIN SELECT order_no
FROM "order"
JOIN contains USING (order_no)
JOIN product USING (SKU)
WHERE price > 50 AND
EXTRACT(YEAR FROM date) = 2023;

EXPLAIN SELECT order_no, SUM(qty*price)
FROM contains
JOIN product USING (SKU)
WHERE name LIKE 'A%'
GROUP BY order_no;

DROP INDEX IF EXISTS product_name_idx;
DROP INDEX IF EXISTS product_price_idx;
DROP INDEX IF EXISTS order_date_idx;
DROP INDEX IF EXISTS idx_contains_sku;
-----------------------------------------------------------------------------------






--DROP INDEX IF EXISTS product_name_idx;
--DROP INDEX IF EXISTS product_price_idx;
--DROP INDEX IF EXISTS order_date_idx;
--DROP INDEX IF EXISTS idx_contains_sku;
--
--
--CREATE INDEX product_price_idx ON product (price);
--
--CREATE INDEX order_date_idx ON "order" (date);
--
--CREATE INDEX idx_contains_sku ON contains(SKU);
--
--CREATE INDEX product_name_idx ON product (name);


nada
    45.97 66.58 1,69s
    31.73 31.88 1,04s
price   
    45.99 66.41 1,44s
    23.31 23.51 0,9s
date
    4.32 17.55 2,14s
    23.31 23,51 1,09s
sku
    4.29 7.67 1,34s
    6.58 6.73 0,882s
name 
    4.27 7.67 1,44s
    6.58 6.63 0,9s
price e date
    4.29 7.67 1,6s
    6.58 6.66 0,96s
price date e sku
    4.29 7.67 1,59s
    6.58 6.63 0,944s
sku e name
    4.29 7.67 1,85s
    6.58 6.63 1,07s
date sku e name
    4.29 7.67 1,692s
    6.58 6.63 1,035s
tudo
    4.29 7.67 1,698s
    6.68 6.63 1,164s


price -10 2
date  -40 1
    sku   -50 both  primary ?
name  -50 both