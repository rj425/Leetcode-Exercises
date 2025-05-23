-- 1280. Students and Examinations
-- https://leetcode.com/problems/students-and-examinations/description/

# Write your MySQL query statement below
SELECT s.student_id, s.student_name, su.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students AS s 
JOIN Subjects AS su
LEFT JOIN Examinations AS e
ON s.student_id = e.student_id
AND e.subject_name = su.subject_name
GROUP BY student_name, subject_name
ORDER BY student_id, subject_name;
