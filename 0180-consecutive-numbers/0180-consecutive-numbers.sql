/* Write your T-SQL query statement below */
SELECT distinct l1.num ConsecutiveNums from logs l1
join logs l2 on l1.id=l2.id-1 
join logs l3 on l2.id = l3.id -1
where l1.num = l2.num and l3.num = l2.num