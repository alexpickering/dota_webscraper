DotA 2 Hero Stats Scraper
=========================

This scraper collects information from the DotA 2 hero pages and outputs it in a csv.



Inventory
---------

DotA Spider. Run with:
```
scrapy runspider dota_spiders.py -o heroes.csv
```

SQL database creation. Run with:
```
sqlite3 dota.db < setup.sql
```

Google Sheets Uploaded. Run with:
```
./upload_to_gsheets.py heroes.csv
```



SQL Tips
--------

Create most of your setup in a sql file. I have called it `setup.sql`.


To execute a sql file with sqlite3, run:
```
sqlite> .read setup.sql
```

To save the database (for testing), run:
```
sqlite> .save test.db
```

To open an existing database (NOT sql file), run:
```
sqlite> .open test.db
```
