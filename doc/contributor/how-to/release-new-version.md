# How to release a new version of QGreenland Core code

Use `bumpversion` to bump the specified part of the version:

```
$ bumpversion --part={major|minor|patch}
```

Versions should be in one of the following forms:

* `vX.Y.ZalphaN`: An alpha pre-release, e.g. `v1.2.3beta2`
* `vX.Y.ZbetaN`: A beta pre-release, e.g. `v1.2.3alpha2`
* `vX.Y.ZrcN`: A release candidate, e.g. `v1.2.3rc3`.
* `vX.Y.Z`: A final release, e.g. `v1.2.3`.

```{caution}
When using `bumpversion build`, ensure you have already used `bumpversion
prerelease`. Running `bumpversion build` from a final release version number
can result in an incorrect patch number, e.g. `v1.2.304`.
```

Publishing a tag to GitHub will trigger an automated build and publish of the
QGreenland Core package to various mirrors.

Creating a "Release" in GitHub will trigger archival of our code in Zenodo and
issuance of a new DOI. Do _not_ create a "Release" in GitHub until a new
version of the package has been successfully built and pushed to mirrors.
