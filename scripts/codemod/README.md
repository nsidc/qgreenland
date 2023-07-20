# Codemods

Write code to automate transformations of the code.

We used `libcst` to accomplish this.

From this directory, run this command to list some available codemods:

```
python -m libcst.tool list
```

You shouldn't need to use these except in extreme cases! `ruff` and `black` meet our
day-to-day code transformation needs.
