-- Write your query below
select employee_id, 

case 
when employee_id % 2 <> 0 AND name not like 'M%' then salary
else 0 
END AS Bonus 

from employees

order by employee_id