-- 1633. Percentage of Users Attended a Contest
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/

# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(*)*100/(SELECT COUNT(*) FROM Users),2) percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC