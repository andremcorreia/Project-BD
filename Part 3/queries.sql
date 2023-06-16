-- 1
WITH total_values AS (
    SELECT pa.cust_no, SUM(pr.price * co.qty) AS total_value
    FROM pay pa
    JOIN contains co ON pa.order_no = co.order_no
    JOIN product pr ON co.SKU = pr.SKU
    GROUP BY pa.cust_no
)
SELECT DISTINCT c.cust_no, c.name
FROM customer c
JOIN total_values t ON c.cust_no = t.cust_no
WHERE t.total_value = (
    SELECT MAX(total_value)
    FROM total_values
);

-- 2
SELECT DISTINCT e.name
FROM employee e
WHERE NOT EXISTS ( 
    SELECT DISTINCT o.date
    FROM "order" o
    WHERE EXTRACT(YEAR FROM o.date) = 2022
    EXCEPT
    SELECT o.date
    FROM process p
    JOIN "order" o ON p.order_no = o.order_no
    WHERE p.ssn = e.ssn
);
-- if there are no dates left after subtracting the dates
-- in processed orders by this employee, from every date
-- in orders, then the employee has processed on every day with orders

-- 3
SELECT EXTRACT(MONTH FROM o.date) AS month, COUNT(*) AS unpaid_orders
FROM "order" o
LEFT JOIN pay p ON o.order_no = p.order_no
WHERE EXTRACT(YEAR FROM o.date) = 2022
    AND p.order_no IS NULL
GROUP BY month;

