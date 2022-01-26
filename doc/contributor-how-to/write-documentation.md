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
Markdown) and other content (including code with `autodoc` or other
extensions). It converts this content into many output formats including HTML
and PDF.

Sphinx's configuration is kept at `doc/conf.py`.


### Read the Docs

_Read the Docs_ is a documentation building and hosting service. It can use
Sphinx or MkDocs under the hood, and we chose Sphinx. It runs automatically in
response to changes in GitHub. It is configured by `.readthedocs.yml` at the
root of this repository.

When Read the Docs builds our documentation, it uses the Python environment
defined by `doc/requirements.txt`.


### reStructuredText

[Start
here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
to learn about writing reStructuredText for Sphinx documentation.


### MyST Markdown extension

[Start here](https://myst-parser.readthedocs.io) to learn about writing
Markdown for Sphinx documentation. Markdown is supported out of the box by Read
the Docs.


## How to add a new documentation page

* Is this new content a [How To](https://diataxis.fr/how-to-guides/), a
  [Tutorial](https://diataxis.fr/tutorials/), [Reference
  material](https://diataxis.fr/reference/), or a [Discussion
  topic](https://diataxis.fr/explanation/)? Ensure your document is in the
  correct directory and written for the correct audience.
* Write your documentation in Markdown, unless you're writing a page that must
  be majority reStructuredText, such as an `index.rst` for a new group of pages.
* Ensure your documentation page starts with a top-level header. This is the
  title of the page.
* Use `inv docs.watch` to build documentation on every edit and view your
  changes in the browser.
* Create a pull request. GitHub will trigger a build on Read the Docs which you
  can view by clicking "details" for the Read the Docs check.


## How to update an existing documentation page

* Is this new content a [How To](https://diataxis.fr/how-to-guides/), a
  [Tutorial](https://diataxis.fr/tutorials/), [Reference
  material](https://diataxis.fr/reference/), or a [Discussion
  topic](https://diataxis.fr/explanation/)? Ensure your document is in the
  correct directory and written for the correct audience.
* Ensure your new content fits appropriately with surrounding content.
* Use `inv docs.watch` to build documentation on every edit and view your
  changes in the browser.
* Create a pull request. GitHub will trigger a build on Read the Docs which you
  can view by clicking "details" for the Read the Docs check.


## Documentation styles

We have created the following styles to use when referring to QGIS elements and menu paths:
* Any reference to a QGIS user interface element will be bolded. e.g.: "Navigate to 
  **Settings -> User Profiles -> Open Active Profile Folder** to get the directory path" or 
  "Use the **Layers Panel** to change the order of the layers".

* Menu paths are delimited by ->, e.g.: Settings -> User Profiles -> Open Active Profile Folder
