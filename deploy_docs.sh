#!/bin/bash
git checkout master
cd docs
make html
cd ..
git checkout gh-pages
cp -r docs/build/html/* .
rm -r docs code
git add .
git commit -m "Update documentation"