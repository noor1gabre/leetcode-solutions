with cte as
(select  mr.* , u.name , m.title
from MovieRating mr
LEFT JOIN Users u
ON mr.user_id = u.user_id
LEFT JOIN Movies m
ON mr.movie_id = m.movie_id
)
(   
    select name as results
    from cte 
    group by name
    order by count(*) desc ,name
    limit 1
)
union all
(
    select title
    from cte 
    where DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
    group by  title
    order by AVG(rating) desc, title
    limit 1
)