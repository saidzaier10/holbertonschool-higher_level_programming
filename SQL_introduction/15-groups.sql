-- Create a query that counts the number of records with the same score in the second_table table, and displays the result in descendant order.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
