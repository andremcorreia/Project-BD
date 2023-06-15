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
-- sku
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

DROP INDEX IF EXISTS idx_contains_sku;

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