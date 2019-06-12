#!/bin/sh
make publish
if [ $? == 0 ]; then
echo "hardcode.today" > ./output/CNAME
ghp-import output
git push -f git@github.com:Gondnat/gnodnate.github.io.git gh-pages:master
fi