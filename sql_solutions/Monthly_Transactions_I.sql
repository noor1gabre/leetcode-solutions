select CONCAT(YEAR(trans_date), '-', LPAD(MONTH(trans_date), 2, '0')) AS month,
country,
count(*) as trans_count,
COUNT(CASE WHEN state = 'approved' THEN 1 END) as approved_count,
SUM(amount) AS trans_total_amount,
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY 
    CONCAT(YEAR(trans_date), '-', LPAD(MONTH(trans_date), 2, '0')),
    country
ORDER BY 
    month, country;