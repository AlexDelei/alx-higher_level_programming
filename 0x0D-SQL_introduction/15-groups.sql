USE hbtn_0c_0; -- Replace 'hbtn_0c_0' with the actual database name passed as an argument

SELECT score, COUNT(*) AS 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
