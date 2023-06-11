# Pandas Python
There are two core objects in pandas: the DataFrame and the Series.

---
---

## DataFrame

A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column

    `pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})`

    `pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})`

---
---

## Series

A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:

    `pd.Series([1, 2, 3, 4, 5])`