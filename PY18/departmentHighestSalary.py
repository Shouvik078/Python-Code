# Department Highest Salary

# select d.name as Department, e.name as Employee,salary
# from Employee e
# inner join Department d ON e.departmentId=d.id
# where (e.departmentId,salary) in (
# Select departmentId,max(salary)
# from Employee
# group by 1
# )