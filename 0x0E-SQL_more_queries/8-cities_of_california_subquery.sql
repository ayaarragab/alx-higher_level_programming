-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM hbtn_0d_usa.cities
WHERE cities.id = (
    SELECT state_id
    FROM hbtn_0d_usa.states
    WHERE hbtn_0d_usa.states.name = 'California'
)
ORDER BY cities.id ASC
;
