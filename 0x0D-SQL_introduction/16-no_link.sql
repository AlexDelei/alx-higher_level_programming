USE hbtn_0c_0; -- Replace 'hbtn_0c_0' with the actual database name passed as an argument

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
