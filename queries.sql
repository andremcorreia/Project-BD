SELECT c.customer_name, o.order_no
FROM customer c
NATURAL JOIN "order" o ON c.cust_no = o.cust_no
WHERE o.order_date >= '2023-01-01' AND o.order_date <= '2023-12-31'

SELECT o.order_no
FROM contains ct
NATURAL JOIN product p ON ct.sku = p.sku
WHERE p.price > 50;

