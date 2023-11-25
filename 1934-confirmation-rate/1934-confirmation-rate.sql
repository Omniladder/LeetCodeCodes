/* Write your T-SQL query statement below */

SELECT signups.user_id, 
cast(cast(sum(case when action = 'confirmed' then 1 else 0 end) as decimal (3,2)) / count(*) as decimal (3,2)) confirmation_rate
from signups left outer join Confirmations on signups.user_id = confirmations.user_id
group by signups.user_id 