-- BOT 2
SELECT
  p.SKU,
  COALESCE(SUBSTRING(cust.address FROM E'\\d{4}-\\d{3} (.+)$'), 'Global') AS city,
  EXTRACT(YEAR FROM o.date) AS year,
  EXTRACT(MONTH FROM o.date) AS month,
  EXTRACT(DAY FROM o.date) AS day_of_month,
  to_char(o.date::date, 'Day') AS day_of_week,
  SUM(c.qty) AS total_quantity,
  SUM(c.qty * p.price) AS total_value
FROM product_sales ps
JOIN product p ON ps.SKU = p.SKU
JOIN "order" o ON ps.order_no = o.order_no
JOIN customer cust ON o.cust_no = cust.cust_no
WHERE EXTRACT(YEAR FROM o.date) = 2022
GROUP BY ROLLUP (p.SKU, city, year, month, day_of_month, day_of_week)
HAVING (
  city IS NOT NULL
  AND year IS NOT NULL
  AND month IS NOT NULL
  AND day_of_month IS NOT NULL
  AND day_of_week IS NOT NULL
)
ORDER BY p.SKU, city, year, month, day_of_month, day_of_week;

-- BOT 2

SELECT
  EXTRACT(MONTH FROM o.date) AS month,
  to_char(o.date::date, 'Day') AS day_of_week,
  AVG(ps.total_value) AS average_daily_value
FROM product_sales ps
JOIN "order" o ON ps.order_no = o.order_no
WHERE EXTRACT(YEAR FROM o.date) = 2022
AND EXTRACT(MONTH FROM o.date) IS NOT NULL
AND day_of_week IS NOT NULL
GROUP BY CUBE (month, day_of_week)
ORDER BY month, day_of_week;
