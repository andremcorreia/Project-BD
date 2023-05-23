-- Ex 1
-- 1.	List the name of all customers who placed orders containing higher priced products than €50 in the year 2023.
-- π_name (σ_price > 50 ∧ date ≥ '2023-01-01' ∧ date ≤ '2023-12-31' (customer ⨝ "order") ⨝ contains) ⨝ π_sku_price (product)))))

SELECT c.customer_name
FROM customer c
JOIN "order" o ON c.cust_no = o.cust_no
JOIN contains ct ON o.order_no = ct.order_no
JOIN product p ON ct.sku = p.sku
WHERE p.price > 50 AND EXTRACT(YEAR FROM o.order_date) = 2023; -- >= '2023-01-01' AND o.order_date <= '2023-12-31';


-- Ex 2
-- 2.	List the name of all employees who work in warehouses and not in offices and processed orders in January 2023.
-- π_name (σ(date ≥ "2023-01-01" ∧ date ≤ "2023-01-31") ((employee ⨝ works) ⨝ process) ⨝ order) ⋂ warehouse) - office)

SELECT e.employee_name
FROM employee e
JOIN works w ON e.ssn = w.ssn
JOIN process p ON e.ssn = p.ssn
JOIN "order" o ON p.order_no = o.order_no
WHERE w.workplace_address IN (SELECT warehouse_address FROM warehouse) 
    AND w.workplace_address NOT IN (SELECT office_address FROM office) 
    AND EXTRACT(YEAR FROM o.order_date) = 2023
    AND EXTRACT(MONTH FROM o.order_date) = 1;

-- Ex 3
-- 3.	Indicate the name of the bestselling product.

SELECT p.product_name
FROM product p
JOIN contains c ON c.sku = p.sku
JOIN sale s ON s.order_no = c.order_no
GROUP BY p.sku
ORDER BY SUM(c.qty) DESC
LIMIT 1;


-- Ex 4
-- 4.	Indicate the total value of each sale made.
SELECT s.order_no, SUM(c.qty * p.price) AS total_value
FROM sale s
JOIN contains c ON c.order_no = s.order_no
JOIN product p ON p.sku = c.sku
GROUP BY s.order_no;