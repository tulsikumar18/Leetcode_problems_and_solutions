# Write your MySQL query statement below



SELECT s.name
FROM SalesPerson s 
WHERE s.sales_id NOT IN(

        SELECT o.sales_id
        FROM Company c
        JOIN Orders o
        ON c.com_id = o.com_id
        WHERE c.name = 'RED'
)


