# Pseudo-SQL: grouping and aggregates

Aggregate functions: `COUNT`, `SUM`, `MIN`, `MAX`, `AVG`.
Grouping — `GROUP BY`, group filtering — `HAVING`.

## How many books in each genre

```query
FROM notes/samples/books
GROUP BY genre
SELECT genre, COUNT(*)
ORDER BY COUNT(*) DESC
```

## Full summary by genre

```query
FROM notes/samples/books
GROUP BY genre
SELECT genre, COUNT(*), SUM(pages), AVG(pages), MIN(year), MAX(year)
ORDER BY COUNT(*) DESC
```

## Average rating and length by genre

```query
FROM notes/samples/books
GROUP BY genre
SELECT genre, AVG(rating), AVG(pages)
ORDER BY AVG(rating) DESC
```

## Overall totals for the whole library (no GROUP BY)

```query
FROM notes/samples/books
SELECT COUNT(*), SUM(pages), AVG(pages), MIN(pages), MAX(pages)
```

## Totals for read books only

```query
FROM notes/samples/books
WHERE read = true
SELECT COUNT(*), SUM(pages), AVG(rating)
```

## Genres with more than one book (HAVING on an aggregate from SELECT)

```query
FROM notes/samples/books
GROUP BY genre
SELECT genre, COUNT(*), SUM(pages)
HAVING COUNT(*) > 1
ORDER BY SUM(pages) DESC
```

## Genres with a total length > 1000 pages
### (HAVING on an aggregate that isn't in SELECT — computed behind the scenes)

```query
FROM notes/samples/books
GROUP BY genre
SELECT genre, COUNT(*)
HAVING SUM(pages) > 1000
```

## Grouping by the "read" flag

```query
FROM notes/samples/books
GROUP BY read
SELECT read, COUNT(*), AVG(rating)
```
