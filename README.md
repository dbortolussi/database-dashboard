# DanielBortolussi

## Dashboard: Academic Conference App

### Widgets:

1. View relevance to keyword by university
  - Order by KRC for all faculty, adjustable count, size of point = number of faculty
2. View relevance to keyword by faculty with publications in the last k years
  - Order by KRC, provide name, university, and email
3. View most related keywords
  - Retrieve top 5 keywords that appear most frequently with given keyword, display in graph
4. View most relevant papers to keyword in given timeframe
  - Order by KRC for each paper, also get authors, adjustable slide for how recent to search
5. Add/Update publication
  - Add new publication with all fields
  - Search for id based on title, return all fields, update based on id
6. Update faculty score
  - Search for id based on name, return all fields, update based on id

### Techniques:

1. Index on keyword
2. Constraint on adding publication
3. Trigger on updating faculty score

