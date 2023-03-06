https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

``` SQL
SELECT (CASE WHEN Students.marks > 69 THEN Students.name ELSE NULL END),Grades.grade,Students.marks
FROM Students
JOIN Grades ON students.marks BETWEEN Grades.min_mark AND Grades.max_mark
ORDER BY 2 DESC, 1,3