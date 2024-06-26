FROM mysql:8.0.25

COPY .my.cnf /root/.my.cnf
COPY 0-privileges.sql /docker-entrypoint-initdb.d/
COPY 1-create_user.sql /docker-entrypoint-initdb.d/
COPY 2-create_read_user.sql /docker-entrypoint-initdb.d/
COPY 3-force_name.sql /docker-entrypoint-initdb.d/
COPY 4-never_empty.sql /docker-entrypoint-initdb.d/
COPY 5-unique_id.sql /docker-entrypoint-initdb.d/
COPY 6-states.sql /docker-entrypoint-initdb.d/
COPY 7-cities.sql /docker-entrypoint-initdb.d/
COPY 8-cities_of_california_subquery.sql /docker-entrypoint-initdb.d/
COPY 9-cities_by_state_join.sql /docker-entrypoint-initdb.d/
COPY 10-genre_id_by_show.sql /docker-entrypoint-initdb.d/
COPY 11-genre_id_all_shows.sql /docker-entrypoint-initdb.d/
COPY 12-no_genre.sql /docker-entrypoint-initdb.d/
COPY 13-count_shows_by_genre.sql /docker-entrypoint-initdb.d/
COPY 14-my_genres.sql /docker-entrypoint-initdb.d/
COPY 15-comedy_only.sql /docker-entrypoint-initdb.d/
COPY 16-shows_by_genre.sql /docker-entrypoint-initdb.d/
