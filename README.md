# web-scrapers

Few web scrapers which prints weekly menu for Marche Soupson store [soupson.ca](http://www.soupson.ca/?lang=en).

# Conky integration

One of these script could be easily used in conky:

![screenshot.png](screenshot.png)


# Python

You need to have `requests` and `Beautiful soup` installed:

```bash
$ apt-get install python-requests
$ apt-get install python-bs4
```

The menu could be printed to the output, or to the file by providing `file` option to the call:

```bash
$ python soupson.py
Monday: Beet and Fennel
Tuesday: Sweet Potato and Lentil
Wednesday: Classic Split Pea Soup
Thursday: Green Vegetable Medley
Friday: HARIRA!
```

```bash
$ python soupson.py file
$ cat menu
Monday: Beet and Fennel
Tuesday: Sweet Potato and Lentil
Wednesday: Classic Split Pea Soup
Thursday: Green Vegetable Medley
Friday: HARIRA!
```

# Node

Install dependencies by running `npm install` and the use it:

```bash
$ node soupson.js
.-----------------------------------------.
| Weekly menu from October 3 to October 7 |
|-----------------------------------------|
| Monday    | Beet and Fennel             |
| Tuesday   | Sweet Potato and Lentil     |
| Wednesday | Classic Split Pea Soup      |
| Thursday  | Green Vegetable Medley      |
| Friday    | HARIRA!                     |
'-----------------------------------------'
```
