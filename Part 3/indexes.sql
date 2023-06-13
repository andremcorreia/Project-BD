
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