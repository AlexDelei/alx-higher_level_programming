-- lists all the genres of the show Dexter

SELECT tv_genres.name AS name FROM tv_shows
JOIN tv_genres ON tv_shows.id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
