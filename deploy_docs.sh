#!/bin/bash
git checkout master
cd docs
make html
cd ..
git checkout gh-pages
cp -r docs/build/html/* .
rm -r docs *py README.md LICENSE
git add .
PRE_COMMIT_ALLOW_NO_CONFIG=1 git commit -m "Update documentation"
git push -u origin gh-pages
git checkout master