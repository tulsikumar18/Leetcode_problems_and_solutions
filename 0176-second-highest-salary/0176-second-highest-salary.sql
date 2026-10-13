# Write your MySQL query statement below


With second_highest_sal AS (

    SELECT  Distinct salary, 
            DENSE_RANK() OVER(ORDER BY salary DESC) AS d_rnk
    FROM Employee 
)

SELECT (SELECT salary 
        FROM second_highest_sal
        WHERE d_rnk = 2
) AS SecondHighestSalary;



