-- OLAP 1
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

-- OLAP 2
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