select distinct city from station
WHERE lower(substr(city,1,1)) not in ('a','e','i','o','u');
