# Lambda School Data Science - Unit 3 - Sprint 2


## SQL and Databases for Data Science


What does “data” look like? If you try to picture it, you probably see rows and columns - a spreadsheet or CSV, that can be conveniently loaded with pandas and cleaned and analyzed from there. As a data scientist, this will often be the form you want your data to be in - but it’s probably not how your data started.

Most modern data is generated automatically by human interaction with a web-backed application - every app they take, every click they make, all travels over a network and is saved by the server. Though in the rawest of forms this may be a log file, in most cases where it really goes is a database.

So, what is a database? A place for data! If it’s relational, it’s actually still pretty close to that rows and columns picture, though with some important additional functionality. These databases are commonly accessed using SQL - Structured Query Language - a standard based on relational algebra, and a useful tool known not just by data scientists but by software engineers, MBAs, and more.

If it’s so-called “NoSQL”, then it’s most likely a document-oriented database (or document store) - which, despite the glamor, is essentially a bunch of key-value pairs. What key-value pair object are you already familiar with? Python dicts!

In this sprint we will learn about both of the above paradigms, and how the separation between them is not as bright a line as you may think.
