-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/

# Write your MySQL query statement below
SELECT V.customer_id, COUNT(V.customer_id) AS count_no_trans FROM Visits V LEFT JOIN Transactions T ON V.visit_id = T.visit_id WHERE T.transaction_id is null GROUP BY V.customer_id;

