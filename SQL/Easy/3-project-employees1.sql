-- 1075. Project Employees I
-- https://leetcode.com/problems/project-employees-i/description/

# Write your MySQL query statement below
SELECT p.project_id, ROUND(SUM(e.experience_years)/COUNT(*),2) as average_years
FROM Project p 
LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY project_id