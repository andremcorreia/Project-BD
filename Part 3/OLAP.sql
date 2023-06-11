SELECT
  SKU,
  city,
  COALESCE(year, 'Total') AS year,
  COALESCE(month, 'Total') AS month,
  COALESCE(day_of_month, 'Total') AS day_of_month,
  COALESCE(day_of_week, 'Total') AS day_of_week,
  SUM(qty) AS total_quantity,
  SUM(total_price) AS total_sales
FROM
  product_sales
WHERE
  year = 2022
GROUP BY
  GROUPING SETS ((SKU, city, year, month, day_of_month, day_of_week), ())
ORDER BY
  SKU, city, year, month, day_of_month, day_of_week;




SELECT
  year,
  month,
  day_of_week,
  AVG(total_sales) AS average_daily_sales
FROM
  (SELECT
    year,
    month,
    day_of_week,
    SUM(total_price) AS total_sales
  FROM
    product_sales
  WHERE
    year = 2022
  GROUP BY
    year, month, day_of_week, day_of_month) AS subquery
GROUP BY
  GROUPING SETS ((year, month, day_of_week), ())
ORDER BY
  year, month, day_of_week;

