#!/bin/sh
pelican content
echo "thnuth.com" > ./output/CNAME
ghp-import output
git push -f https://github.com/Gnodnate/gnodnate.github.io.git gh-pages:master
