#!/bin/bash
wget -q https://github.com/cpmpercussion/cpm-website-publications-list/raw/master/publications.bib -O ./_bibliography/publications.bib
sed -i'' -e '/@/s/://g' ./_bibliography/publications.bib
