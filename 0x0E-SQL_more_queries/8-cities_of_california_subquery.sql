-- print list of cities of california that can be found in the current database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California");
