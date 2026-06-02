# 📦 Sample notes

A set of demonstration notes: a dataset, input forms and pseudo-SQL queries.
Open the files in **view mode** so the forms and queries render.

## What's inside

| File / folder | What it shows |
|---------------|---------------|
| `books/` | A dataset of 10 books — md notes with frontmatter (title, author, genre, year, pages, rating, read, tags). The queries run over these. |
| `form_add_book.md` | A **form** (`destination: note`) — adds a new book as an md file in `books/`. |
| `form_review_db.md` | A **form** (`destination: database`) — saves a review into the DB (`form_records`, catalog `reviews`). |
| `queries_basic.md` | Basic queries: `WHERE`, `SELECT`, `ORDER BY`, `LIMIT`, `CONTAINS`, `LIKE`, `AND`. |
| `queries_aggregate.md` | Grouping and aggregates: `GROUP BY`, `COUNT/SUM/MIN/MAX/AVG`, `HAVING`. |
| `queries_database.md` | Queries over form records: `FROM database/reviews`. |

## Where to start

1. Open **`queries_basic.md`** and **`queries_aggregate.md`** in view mode — the
   queries immediately return results over the `books/` dataset.
2. Open **`form_add_book.md`** in view mode, fill it in and save — a new book
   appears and shows up in the query results.
3. Open **`form_review_db.md`**, save a couple of reviews, then look at
   **`queries_database.md`** — the data from the DB appears there.

## The books/ dataset (for reference)

10 books, 4 genres: `sci-fi` (3), `fantasy` (3), `dystopia` (2), `tech` (2).
Fields: `title`, `author`, `genre`, `year`, `pages`, `rating` (1-5),
`read` (true/false), `tags` (list).
