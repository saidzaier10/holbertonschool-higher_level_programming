-- This query is used to find the scores of the students who have no name. The query should display the score and name of the students in descending order of their scores.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
