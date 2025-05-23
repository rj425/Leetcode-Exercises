-- 620. Not Boring Movies
-- https://leetcode.com/problems/not-boring-movies/description/

# Write your MySQL query statement below
SELECT * FROM Cinema c WHERE (c.id % 2) = 1 AND c.description != 'boring' ORDER BY c.rating DESC;