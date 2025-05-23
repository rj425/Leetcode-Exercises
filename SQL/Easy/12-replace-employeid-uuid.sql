-- 1378. Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/

# Write your MySQL query statement below
SELECT b.unique_id, a.name FROM Employees AS a LEFT JOIN EmployeeUni AS b ON a.id = b.id;