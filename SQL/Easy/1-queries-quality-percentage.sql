-- 1211. Queries Quality and Percentage
-- https://leetcode.com/problems/queries-quality-and-percentage/description/

# Write your MySQL query statement below
SELECT query_name, 
ROUND(AVG(rating/position),2) quality, 
ROUND(AVG(rating<3)*100,2) poor_query_percentage
FROM Queries
GROUP BY query_name