-- 1193. Monthly Transactions I
-- https://leetcode.com/problems/monthly-transactions-i/description/

# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date,'%Y-%m') month, 
country, 
COUNT(*) trans_count,
SUM(IF(state='approved',1,0)) approved_count,
SUM(amount) trans_total_amount,
SUM(IF(state='approved',amount,0)) approved_total_amount
FROM Transactions 
GROUP BY month, country