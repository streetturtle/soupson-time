#!/bin/bash

curl -s 'http://www.soupson.ca/?lang=en' |  # get page
grep -m 1 -A 10 'class="entry-content"' |   # find first entry of entry-content class
grep '<p>\w' | tr -d '</p>'                 # replace paragraph tags

