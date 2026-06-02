---
type: form
destination: note
catalog: ./samples/books/
fields:
  - title: ["Title", string, 80]
  - author: ["Author", string, 60]
  - genre: ["Genre", list, select, [sci-fi, fantasy, dystopia, tech, other]]
  - year: ["Year published", integer, 0]
  - pages: ["Pages", integer, 0]
  - rating: ["Rating (1-5)", list, select, [1, 2, 3, 4, 5]]
  - read: ["Read", boolean, 0]
  - tags: ["Tags", list, multi-select, [classic, space, magic, adventure, politics, programming, craft, science, cyberpunk]]
  - summary: ["Short summary", text, 0]
---

<!--
This is a form (type: form).

In VIEW mode this note is shown as an input form with "Save" / "Cancel" buttons.
In EDIT mode you see this source text.

destination: note  -> saving creates a new md file
catalog: ./samples/books/ -> the file lands in the books folder and is immediately
                             picked up by the queries FROM notes/samples/books.

The file name comes from the first non-empty string field (here — "Title").
-->
