-- this script will print all the cities of California that can be found in the current database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id;
