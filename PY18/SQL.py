# Calculate N th Salary 


# with cte as (
#       select *, 
#       dense_rank() over(order by salary desc) as rnk
#       from employee
#       )
#       select max(case when rnk=N then salary else null end) Nth_Salary
#       from cte 