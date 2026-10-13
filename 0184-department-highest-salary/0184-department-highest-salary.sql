# Write your MySQL query statement below

WITH dept_hiSal AS (

    SELECT e.name AS Employee, e.salary AS Salary , d.name AS Department,
            DENSE_RANK() OVER(
                PARTITION BY e.departmentId 
                ORDER BY e.salary DESC
            ) AS d_rnk
    FROM employee e
    JOIN Department d
    ON e.departmentId = d.id
)

SELECT  Department,
       Employee, Salary

FROM dept_hiSal
WHERE d_rnk = 1;

