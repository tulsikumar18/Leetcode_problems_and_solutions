# Write your MySQL query statement below

-- SELECT s.name

-- FROM SalesPerson s 
-- LEFT JOIN Orders o 
-- ON s.sales_id = o.sales_id 

-- JOIN company c 
-- ON 


-- WHERE o.sales_id IS NULL  and c.name != 'RED';



SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c
        ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);