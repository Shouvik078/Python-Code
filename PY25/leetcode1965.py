
# #  LEETCODE 1965
# # Write your MySQL query statement below


# SELECT employee_id FROM Employees WHERE employee_id NOT IN (SELECT employee_id FROM salaries)
# UNION 
# SELECT employee_id FROM salaries WHERE employee_id NOT IN (SELECT employee_id FROM employees)
# ORDER BY employee_id