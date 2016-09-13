#!/bin/sh
pelican content
ghp-import output
git push -f https://github.com/Gnodnate/gnodnate.github.io.git gh-pages:master
