# Testing CI and github-pages

## Testing with Continous Itegration (CI)
We would like to run our tests every time we push in order to make sure that any update to the code does not break any core functionality.

Follow the [instructions](https://docs.travis-ci.com/user/tutorial/) on how to set up travis-ci.

For more information about how to test your python project check out the [documentation](https://docs.travis-ci.com/user/languages/python/)

Add a badge with the information about whether test passed or not. In my case this was

[![Build Status](https://travis-ci.com/finsberg/vector3D.svg?branch=master)](https://travis-ci.com/finsberg/vector3D)


## Creating documentation for your code.

We will use `sphinx` to generate documentation and we will publish the documentation using github pages. 
Create a the directory `docs` where we will put the documentation
```
mkdir docs
cd docs
```
Now we run the `sphinx-quickstart` which is the first step in generating documentation. This will ask you some questions, and I will reply as follows

```
$ sphinx-quickstart
Welcome to the Sphinx 1.8.3 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:

The project name will occur in several places in the built documentation.
> Project name: Vector3D
> Author name(s): Henrik Finsberg
> Project release []: 2.0

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]:

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:
Indicate which of the following Sphinx extensions should be enabled:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]: n

Creating file ./source/conf.py.
Creating file ./source/index.rst.
Creating file ./Makefile.

Finished: An initial directory structure has been created.

You should now populate your master file ./source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

You can look at your documentation by running
```
make html
python -m http.server
```
Then open a web-browser and go to http://localhost:8000, and navigate to build/html.

### Creating API documentation

Now we will make the documentation for our python package

```
sphinx-apidoc -o source/ ..
```

If you now try to run `make html` then you will get the following error:

```
WARNING: autodoc: failed to import module 'test_vector'; the following exception was raised:
No module named 'test_vector'
WARNING: autodoc: failed to import module 'vector'; the following exception was raised:
No module named 'vector'. 
```

To fix this open `source/conf.py` and add the following lines at the top
```Python
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
```
Now if you try to run `make html`, you will get a new warining saying: `Unexpected section title`, and this is because I have documented the code using the numpy style, which is not default. Open source/conf.py and add `sphinx.ext.napoleon` to the list called extensions. Let us also change the html theme. Scroll down and set `html_theme = "sphinx_rtd_theme"`, and run pip install sphinx-rtd-theme.

You can look at your documentation by running
```
make html
python -m http.server
```
Then open a web-browser and go to http://localhost:8000, and navigate to build/html.

Now you can also add some more information to `source/index.rst` in order to display some more information on the index page. I have in this example converted the README file to restructured text (.rst) and pasted this in.

### Building documenation that will be hosted on github pages

Create a new branch called `gh-pages`
```
git checkout -b gh-pages
```
Now delete everything in the repo and commit it
```
rm -r *
git add -u
git commit -m "Remove all files"
```
Now go back to the `master` brach and build the documentation.
```
git checkout master
cd docs
make html
```
This will build the html documentation. Now checkout the `gh-pages` branch again, move the html files to the root folder and add them.
```
git checkout gh-pages
mv docs/build/html/* .
rm -r docs
git add .
commit -m "Adding documentation"
```

All steps can be summarized in the following bash script
```shell
git checkout master
cd docs
make html
cd ..
git checkout gh-pages
cp -r docs/build/html/* .
rm -r docs *py README.md LICENSE
git add .
git commit -m "Update documentation"
git push -u origin gh-pages
git checkout master
```
Finally go to GitHub, click on settings. Scroll down to the section called GitHub pages, and select `gh-pages branch`.
It will now tell you that your site will be published at https://username.github.io/vector3D, in my case this is https://finsberg.github.io/vector3D

### Problems with style-sheets
If your site is displaying but the styling is wrong then you can try to add an empty file called `.nojekyll` to the `gh-pages` branch, i.e
```
git checkout gh-pages
touch .nojekyll
git add .nojekyll
git commit -m "Add .nojekyll"
git push -u origin gh-pages
git checkout master
```

# Installing a pre-commit hooks

A pre-commit hook is a hook (or a small program) that runs every time you try to commit to you repository. In this tutorial we will show how you can set up a pre-commit hook that runs black and flake8 every time you try to commit. If black and flake8 gives you thumbs up, then your changes will be commited, otherwise you will be asked to revise your code and change it so that black and flake8 passes. 


First you need to install the `pre-commit` package (https://pre-commit.com).
Therearefter you need to add a pre-commit-config file to your repository.
Add a file called `.pre-commit-config.yaml` with the following content (taken from https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/)
```
-   repo: https://github.com/ambv/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.7
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
    - id: flake8
```
Now commit this file to your repository and run the command `pre-commit install`