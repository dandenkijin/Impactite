# Pseudo-SQL: basic queries

These queries run over the books dataset in `notes/samples/books`.
Open this note in **view mode** — the `query` blocks render as tables.

## All books (selected fields)

```query
FROM samples/books
SELECT title, author, genre, year
ORDER BY year
```

## Read books only

```query
FROM samples/books
WHERE read = true
SELECT title, author, rating
ORDER BY rating DESC
```

## Highly rated books (numeric comparison)

```query
FROM samples/books
WHERE rating >= 5
SELECT title, genre, pages
ORDER BY pages DESC
```

## Thick books (> 400 pages), top 5

```query
FROM samples/books
WHERE pages > 400
SELECT title, pages, genre
ORDER BY pages DESC
LIMIT 5
```

## Sci-fi published after 1980 (two conditions via AND)

```query
FROM samples/books
WHERE genre = sci-fi AND year > 1980
SELECT title, author, year
```

## Search by a tag (membership in a list)

```query
FROM samples/books
WHERE tags CONTAINS classic
SELECT title, year, tags
```

## Search by substring in the author (LIKE — case-insensitive)

```query
FROM samples/books
WHERE author LIKE tolkien
SELECT title, author, year
```

## All fields + implicit file / path

```query
FROM samples/books
WHERE genre = tech
SELECT file, title, path
```
