#!/bin/sh
pelican content
echo "hardcode.today" > ./output/CNAME
ghp-import output
git push -f git@github.com:Gondnat/gnodnate.github.io.git gh-pages:master
