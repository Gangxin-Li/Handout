https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

SELECT CITY.name
FROM CITY
JOIN COUNTRY ON COUNTRY.code = CITY.countrycode
WHERE CONTINENT = 'Africa'



https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

SELECT COUNTRY.continent,FLOOR(AVG(CITY.population))
FROM COUNTRY
JOIN CITY ON CITY.countrycode = COUNTRY.code
GROUP BY COUNTRY.continent

