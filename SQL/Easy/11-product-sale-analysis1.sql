-- 1068. Product Sales Analysis I
-- https://leetcode.com/problems/product-sales-analysis-i/description/

# Write your MySQL query statement below
SELECT P.product_name, S.year, S.price FROM Sales S LEFT JOIN Product P ON S.product_id = P.product_id;