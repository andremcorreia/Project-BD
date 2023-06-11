DROP VIEW IF EXISTS product_sales;

CREATE VIEW product_sales(SKU, order_no, qty, total_price, year, month, day_of_month, day_of_week, city)
AS 
SELECT p.SKU,
       o.order_no,
       c.qty,
       c.qty * p.price AS total_price
       EXTRACT(YEAR FROM o.date) AS year,
       EXTRACT(MONTH FROM o.date) AS month,
       EXTRACT(DAY FROM o.date) AS day_of_month,
       to_char(o.date::date, 'Day') AS day_of_week
       SUBSTRING(cust.address from E'\\d{4}-\\d{3} (.+)$' ) AS city
FROM product p
JOIN contains c ON p.SKU = c.SKU
JOIN "order" o ON c.order_no = o.order_no
JOIN pay pa ON pa.order_no = o.order_no
JOIN customer cust ON pa.cust_no = cust.cust_no
