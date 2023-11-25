/* Write your T-SQL query statement below */

SELECT cast(year(trans_date) as varchar(4)) + '-' + right('0' + cast(month(trans_date) as varchar(2)),2) [month], country, count(*) trans_count, 
sum(case when state = 'approved' then 1 else 0 end) approved_count, sum(amount) trans_total_amount, sum(case when state = 'approved' then amount else 0 end) approved_total_amount
from transactions group by  year(trans_date), month(trans_date), country