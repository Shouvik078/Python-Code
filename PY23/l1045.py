# # Write your MySQL query statement below

# with cte as
# (
# select customer_id, count(distinct product_key) as pk
# from Customer 
# group by 1
# )
# select customer_id from cte 
# where pk=(select count(distinct product_key) from product)
# order by 1
