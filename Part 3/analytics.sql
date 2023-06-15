-- 1 ROLLUP
--SELECT
--  p.SKU,
--  COALESCE(SUBSTRING(cust.address FROM E'\\d{4}-\\d{3} (.+)$'), 'Global') AS city,
--  EXTRACT(YEAR FROM o.date) AS year,
--  EXTRACT(MONTH FROM o.date) AS month,
--  EXTRACT(DAY FROM o.date) AS day_of_month,
--  to_char(o.date::date, 'Day') AS day_of_week,
--  SUM(co.qty) AS total_quantity,
--  SUM(co.qty * p.price) AS total_value
--FROM product_sales ps
--JOIN product p ON ps.SKU = p.SKU
--JOIN "order" o ON ps.order_no = o.order_no
--JOIN contains co ON co.order_no = o.order_no
--JOIN customer cust ON o.cust_no = cust.cust_no
--WHERE EXTRACT(YEAR FROM o.date) = 2022
--GROUP BY ROLLUP (p.SKU, cust.address, o.date, city, year, month, day_of_month, day_of_week)
--HAVING (
--  city IS NOT NULL
--  AND year IS NOT NULL
--  AND month IS NOT NULL
--  AND day_of_month IS NOT NULL
--  AND day_of_week IS NOT NULL
--)
--ORDER BY p.SKU, city, year, month, day_of_month, day_of_week;

-- 1 GROUPING SETS
SELECT 
    p.SKU,
    COALESCE(city, 'Overall') AS city,
    COALESCE(month::text, 'Overall') AS month,
    COALESCE(day_of_month::text, 'Overall') AS day_of_month,
    COALESCE(day_of_week, 'Overall') AS day_of_week,
    SUM(c.qty) AS total_quantity,
    SUM(total_price) AS total_sales_value
FROM 
    product_sales
WHERE 
    year = 2022
GROUP BY 
    GROUPING SETS (
           (sku, city), 
           (sku, month), 
           (sku, day_of_month), 
           (sku, day_of_week), 
           (sku)
        ---(p.SKU, city, month, day_of_month, day_of_week),
        ---(p.SKU, city, month, day_of_month),
        ---(p.SKU, city, month),
        ---(p.SKU, city),
        ---(p.SKU),
        ---()
    );

-- 2 GROUP BY
--SELECT
--  EXTRACT(MONTH FROM o.date) AS month,
--  to_char(o.date::date, 'Day') AS day_of_week,
--  AVG(ps.total_price) AS average_daily_value
--FROM product_sales ps
--JOIN "order" o ON ps.order_no = o.order_no
--WHERE EXTRACT(YEAR FROM o.date) = 2022
--AND EXTRACT(MONTH FROM o.date) IS NOT NULL
--AND day_of_week IS NOT NULL
--GROUP BY (o.date, month, day_of_week)
--ORDER BY month, day_of_week;

--WITH daily_sales AS (
--  SELECT
--    o.date,
--    EXTRACT(MONTH FROM o.date) AS month,
--    to_char(o.date::date, 'Day') AS day_of_week,
--    AVG(ps.total_price) AS total_daily_value
--  FROM product_sales ps
--  JOIN "order" o ON ps.order_no = o.order_no
--  WHERE EXTRACT(YEAR FROM o.date) = 2022
--  GROUP BY o.date
--)
--
--SELECT
--  month,
--  day_of_week,
--  SUM(total_daily_value) AS average_daily_value
--FROM daily_sales
--GROUP BY month, day_of_week
--ORDER BY month, day_of_week;

-- 2 GROUPING SETS
SELECT 
    COALESCE(month::text, 'Overall') AS month,
    COALESCE(day_of_week, 'Overall') AS day_of_week,
    AVG(total_price) AS average_daily_sales
FROM 
    product_sales
WHERE 
    year = 2022
GROUP BY 
    GROUPING SETS (
        (month),
        (day_of_week),
        ()
    );



























"""
The provided OLAP (Online Analytical Processing) queries are designed to analyze and aggregate 
data from the given database schema. OLAP queries are used to perform multi-dimensional analysis
of data, allowing users to gain insights and discover trends in their data.
Let's break down the two queries and explain what each of them does.

Query 1:

The first query is designed to provide a detailed summary of product sales,
including information on the SKU (Stock Keeping Unit), city, date, day of the week, total quantity sold, and total sales value.
The query groups the data using the ROLLUP function, which allows for hierarchical aggregation of data.
In this case, the hierarchy is SKU, city, year, month, day_of_month, and day_of_week.

The query first joins multiple tables, including product_sales, product, order, contains, and customer to gather all the necessary information. 
It then filters the data to include only records from the year 2022. 
The GROUP BY ROLLUP clause generates subtotals for each level of the hierarchy, and the HAVING clause filters out rows with NULL values in the specified columns. 
Finally, the query sorts the result by SKU, city, year, month, day_of_month, and day_of_week.

Query 2:

The second query aims to calculate the average daily sales value for each month and day of the week in the year 2022.
This query uses a Common Table Expression (CTE) called 'daily_sales' to first aggregate the total daily sales value for each day in the year 2022. 
The CTE groups the data by order date and calculates the sum of total prices from the product_sales table.

Next, the main query selects the month and day_of_week from the CTE and calculates the average total daily value for each combination of month and day_of_week. 
The result is then grouped by month and day_of_week and sorted by the same columns.

These OLAP queries provide valuable insights into the sales data, allowing users to analyze sales trends, identify patterns, 
and make informed decisions based on the aggregated data.
"""