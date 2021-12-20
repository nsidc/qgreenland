# How to write documentation

Our documentation is written in
[reStructuredText](https://docutils.sourceforge.io/rst.html) and
[Markdown](https://daringfireball.net/projects/markdown/) for the
[Sphinx](https://www.sphinx-doc.org/en/master/) documentation generator. The
[documentation website](https://qgreenland.readthedocs.io/) is built by and
hosted on [Read the Docs](https://readthedocs.org/).

We follow a conceptual framework called [Diátaxis](https://diataxis.fr/) to
write high quality, easy-to-use documentation.

We expected Sphinx and reStructuredText to be difficult to learn, but were
pleasantly surprised. We hope that you will also find it easy and pleasant to
contribute to our documentation. Thank you in advance for your efforts!


## Background information

Our documentation lives in the `doc/` folder. The documentation-generator
config is in `doc/conf.py`. The ReadTheDocs configuration is in
`.readthedocs.yml` file at the root of this repository. The main tables of
contents are expressed in the `doc/index.rst` file.


### Diátaxis

[Diátaxis](https://diataxis.fr/) provides a conceptual framework for targeting
and organizing information in documentation.

Please familiarize yourself with this framework and help us continually improve
the quality of our docs. The best place to start is [this video on
YouTube](https://www.youtube.com/watch?v=t4vKPhjcMZg).


### Sphinx

Sphinx reads documentation (written in reStructuredText or, with an extension,
Markdown) and other content, including code with the `autodoc` extension. It
converts this content into many output formats including HTML and PDF.


### reStructuredText

...


### Read the Docs

...


## How to add a new documentation page

* Is this new content a [How To](TODO), a [Tutorial](TODO), [Reference
  material](TODO), or a [Discussion topic](TODO)? 
* Write your documentation in Markdown, unless you're writing a page that must
  be majority reStructuredText, such as an `index.rst` for a new group of pages.
* Ensure your documentation page starts with a top-level header. This is the
  title of the page.


## How to update an existing documentation page.

* Is this existing content a [How To](TODO), a [Tutorial](TODO), [Reference
  material](TODO), or a [Discussion topic](TODO)? 
* ...
