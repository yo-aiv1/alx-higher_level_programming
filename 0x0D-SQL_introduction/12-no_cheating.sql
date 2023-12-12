-- this script will update the scor of bob to 10 in the table second_table
-- of the current database
UPDATE second_table SET score=10 WHERE name="Bob" ORDER BY score DESC;
