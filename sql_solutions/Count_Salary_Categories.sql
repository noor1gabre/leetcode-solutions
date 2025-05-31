SELECT 
    categories.category,
    COUNT(categorized_accounts.account_id) AS accounts_count
FROM 
    (SELECT 'Low Salary' AS category
     UNION ALL
     SELECT 'Average Salary'
     UNION ALL
     SELECT 'High Salary') AS categories
LEFT JOIN 
    (SELECT 
        account_id,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category
    FROM 
        Accounts) AS categorized_accounts
ON 
    categories.category = categorized_accounts.category
GROUP BY 
    categories.category
ORDER BY 
    categories.category;
