# Pseudo-SQL: queries against the database

The `database` source is the form records with `destination: database`
(the `form_records` table in `.tag_index.db`).

> To get data here, first open **`form_review_db.md`** in view mode, fill in the
> form and press "Save". The record lands in the `reviews` catalog. You can save
> several reviews — then the aggregates will work too.

## All reviews from the `reviews` catalog

```query
FROM database/reviews
SELECT book, reviewer, rating, recommend
ORDER BY rating DESC
```

## Recommended reviews only

```query
FROM database/reviews
WHERE recommend = true
SELECT book, reviewer, rating
```

## High-rated reviews + implicit fields (id, created_at)

```query
FROM database/reviews
WHERE rating >= 4
SELECT id, book, rating, created_at
ORDER BY created_at DESC
```

## Average rating per book (aggregates in the DB)

```query
FROM database/reviews
GROUP BY book
SELECT book, COUNT(*), AVG(rating)
ORDER BY AVG(rating) DESC
```

## Books with more than one review (HAVING)

```query
FROM database/reviews
GROUP BY book
SELECT book, COUNT(*)
HAVING COUNT(*) > 1
```
