-- Ex 1
-- 1.	List the name of all customers who placed orders containing higher priced products than €50 in the year 2023.

SELECT c.name
FROM customer c
JOIN "order" o ON c.cust_no = o.cust_no
JOIN contains ct ON o.order_no = ct.order_no
JOIN product p ON ct.sku = p.sku
WHERE p.price > 50 AND EXTRACT(YEAR FROM o.date) = 2023
GROUP BY c.cust_no;


-- Ex 2
-- 2.	List the name of all employees who work in warehouses and not in offices and processed orders in January 2023.

SELECT e.name
FROM employee e
JOIN works w ON e.ssn = w.ssn
JOIN process p ON e.ssn = p.ssn
JOIN "order" o ON p.order_no = o.order_no
WHERE w.address IN (SELECT "address" FROM warehouse) 
    AND w.address NOT IN (SELECT "address" FROM office) 
    AND EXTRACT(YEAR FROM o.date) = 2023
    AND EXTRACT(MONTH FROM o.date) = 1
GROUP BY e.ssn;

-- Ex 3
-- 3.	Indicate the name of the bestselling product.

SELECT p.name AS best_seller
FROM product p
JOIN contains c ON c.sku = p.sku
JOIN sale s ON s.order_no = c.order_no
GROUP BY p.sku
ORDER BY SUM(c.qty) DESC
LIMIT 1;


-- Ex 4
-- 4.	Indicate the total value of each sale made.

SELECT s.order_no AS sale_number, SUM(c.qty * p.price) AS total_value
FROM sale s
JOIN contains c ON c.order_no = s.order_no
JOIN product p ON p.sku = c.sku
GROUP BY s.order_no;