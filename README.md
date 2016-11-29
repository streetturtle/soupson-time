# Soupson Time

Few web scrapers which prints weekly menu for [Marche Soupson](http://www.soupson.ca/?lang=en).

# Conky integration

One of these scripts could be easily used as conky widget:

![screenshot.png](screenshot.png)


```
...
${execpi 3600 TDY=`date '+%A'`; cat /home/usrnm/.conky/menu | sed s/$TDY/'${color 46B5D3}'"$TDY"'$color'/}
...
```

# Python

You need to have [`requests`](http://docs.python-requests.org/en/master/) and [`Beautiful soup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) installed:

```sh
$ apt-get install python-requests
$ apt-get install python-bs4
```

The menu could be printed to the output:

```sh
$ python soupson.py
Monday: Beet and Fennel
Tuesday: Sweet Potato and Lentil
Wednesday: Classic Split Pea Soup
Thursday: Green Vegetable Medley
Friday: HARIRA!
```

or to the file by providing file name as an option:

```bash
$ python soupson.py menu
$ cat menu
Monday: Beet and Fennel
Tuesday: Sweet Potato and Lentil
Wednesday: Classic Split Pea Soup
Thursday: Green Vegetable Medley
Friday: HARIRA!
```

# Node

Install dependencies and then just run it:

```bash
$ npm install
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
