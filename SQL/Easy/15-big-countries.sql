-- 595. Big Countries
-- https://leetcode.com/problems/big-countries/description/

# Write your MySQL query statement below
SELECT name, population, area from World WHERE area >= 3000000 OR population >= 25000000;