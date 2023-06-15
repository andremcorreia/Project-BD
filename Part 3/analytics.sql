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

-- 2 GROUP BY
SELECT 
    SKU,
    COALESCE(city, 'Globally') AS city,
    COALESCE(month::text, 'Globally') AS month,
    COALESCE(day_of_month::text, 'Globally') AS day_of_month,
    COALESCE(day_of_week, 'Globally') AS day_of_week,
    SUM(qty) AS total_quantity,
    SUM(total_price) AS total_sales_value
FROM 
    product_sales
WHERE 
    year = 2022
GROUP BY 
    GROUPING SETS (
        (SKU, city),
        (SKU, month),
        (SKU, day_of_month),
        (SKU, day_of_week),
        (SKU)
    );


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

-- 2 Grouping sets
SELECT 
    COALESCE(month::text, 'Globally') AS month,
    COALESCE(day_of_week, 'Globally') AS day_of_week,
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