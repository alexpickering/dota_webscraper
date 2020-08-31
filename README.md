Create most of your setup in a sql file. I have called it `setup.sql`.


To execute a sql file with sqlite3, run:
sqlite> .read setup.sql


To save the database (for testing), run:
sqlite> .save test.db


To open an existing database (NOT sql file), run:
sqlite> .open test.db
