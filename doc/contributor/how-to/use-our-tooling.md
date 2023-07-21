# How to use QGreenland development tooling

## Linting and formatting

This project uses [pre-commit](https://pre-commit.com/) for linting and code formatting.
This dependency is already part of the QGreenland Conda environment! To set it up,
simply:

```
pre-commit install
```

This will configure Git hooks which will trigger when you make a commit.


## Testing and other stuff

We use [invoke](https://www.pyinvoke.org/) for other miscellaneous tasks, like:

* Environment locking (`inv env.lock`)
* Interactive docs building (`inv docs.watch`)
* Typechecking (`inv test.typecheck`)
* ... and much, much more!

Use `inv --list` to view a list of available tasks.
