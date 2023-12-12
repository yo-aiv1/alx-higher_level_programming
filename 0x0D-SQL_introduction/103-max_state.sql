-- will print the max temperature of each state (otderd by the state name)
SELECT state, MAX(value) AS max_temp FROM temperatures;
