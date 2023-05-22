-- 1
SELECT c.customer_name
FROM customer c
INNER JOIN "order" o ON c.cust_no = o.cust_no
INNER JOIN contains ct ON o.order_no = ct.order_no
INNER JOIN product p ON ct.sku = p.sku
WHERE p.price > 50 AND o.order_date >= '2023-01-01' AND o.order_date <= '2023-12-31';

-- algebra 1
WITH orders_2023 AS (
    SELECT c.customer_name, o.order_no
    FROM "order" o
    JOIN customer c ON o.cust_no = c.cust_no
    WHERE o.order_date >= '2023-01-01' AND o.order_date <= '2023-12-31'
), products_over_50 AS (
    SELECT c.order_no
    FROM contains c
    JOIN product p ON c.sku = p.sku
    WHERE p.price > 50
)
SELECT DISTINCT o.customer_name
FROM orders_2023 o
JOIN products_over_50 po ON o.order_no = po.order_no;


-- 2
SELECT e.employee_name
FROM employee e
INNER JOIN works w ON e.ssn = w.ssn
INNER JOIN process pr ON e.ssn = pr.ssn
INNER JOIN "order" o ON pr.order_no = o.order_no
WHERE w.department_name = 'Warehouse' AND w.workplace_address <> (
    SELECT workplace_address
    FROM office
) AND o.order_date >= '2023-01-01' AND o.order_date <= '2023-01-31';

-- algebra 2
WITH workers_warehouses AS (
    SELECT w.ssn
    FROM works w
    JOIN (
        SELECT s.workplace_address
        FROM works s
        EXCEPT
        SELECT o.office_address
        FROM office o
    ) wwo ON w.workplace_address = wwo.workplace_address
), orders_jan_2023 AS (
    SELECT p.ssn
    FROM process p
    JOIN "order" o ON p.order_no = o.order_no
    WHERE o.order_date >= '2023-01-01' AND o.order_date <= '2023-01-31'
)
SELECT DISTINCT e.employee_name
FROM workers_warehouses w
JOIN orders_jan_2023 o ON w.ssn = o.ssn
JOIN employee e ON e.ssn = w.ssn;


-- 3
SELECT p.product_name
FROM product p
JOIN contains ct ON p.sku = ct.sku
GROUP BY p.product_name
ORDER BY SUM(ct.qty) DESC
LIMIT 1;

--algebra 3
WITH sales AS (
    SELECT s.order_no
    FROM sale s
    JOIN contains c ON s.order_no = c.order_no
), products_sold AS (
    SELECT p.product_name, c.qty
    FROM sales s
    JOIN product p ON p.sku = c.sku
)
SELECT product_name
FROM (
    SELECT product_name, ROW_NUMBER() OVER (ORDER BY qty DESC) AS rn
    FROM products_sold
) sub
WHERE rn = 1;

-- 4
SELECT o.order_no, SUM(p.price * ct.qty) AS total_value
FROM "order" o
JOIN contains ct ON o.order_no = ct.order_no
JOIN product p ON ct.sku = p.sku
GROUP BY o.order_no;

--algebra 4
WITH sales AS (
    SELECT s.order_no, p.price * c.qty AS total_each_product
    FROM sale s
    JOIN contains c ON s.order_no = c.order_no
    JOIN product p ON c.sku = p.sku
)
SELECT order_no, SUM(total_each_product) AS total
FROM sales
GROUP BY order_no;
