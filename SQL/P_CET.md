P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).

```SQL
WITH RECURSIVE CTE as (
SELECT 20 AS U
UNION ALL
SELECT U - 1 AS U from CTE WHERE U > 1
)
SELECT REPEAT('* ', U)  FROM CTE;
```