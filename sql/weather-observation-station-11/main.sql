SELECT distinct city from station
WHERE lower(substr(CITY,1,1)) not in ('a','e','i','o','u')
OR lower(substr(city, -1,1)) not in ('a','e','i','o','u');
