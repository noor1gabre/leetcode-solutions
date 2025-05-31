SELECT 
    s.user_id,
    ROUND(COUNT(CASE WHEN action = 'confirmed' THEN 1 END) / COUNT(*), 2) AS confirmation_rate
FROM 
    Signups as s
LEFT JOIN
    Confirmations as c ON s.user_id = c.user_id
GROUP BY 
    s.user_id;
