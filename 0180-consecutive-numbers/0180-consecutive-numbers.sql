# Write your MySQL query statement below


WITH three_conseVal AS (
    Select  num , 
            LAG(num,1) OVER(ORDER BY id) AS prev1,
            LAG(num,2) OVER(ORDER BY id) AS prev2
    from Logs
)


SELECT Distinct num AS ConsecutiveNums
FROM three_conseVal
WHERE num = prev1 AND num = prev2;