# Write your MySQL query statement below


-- SELECT user_id, name, mail

-- FROM Users
-- WHERE mail REGEXP_LIKE(mail, [A-Za-z]+[A-Za-z0-9._] * @leetcode[.]com)


select * from Users
where regexp_like(mail, '^[A-Za-z]+[A-Za-z0-9_.-]*@leetcode[.]com$','c')