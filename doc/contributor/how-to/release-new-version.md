# How to release a new version of QGreenland Core code

## 1. Update the CHANGELOG

Ensure that the `CHANGELOG.md` is updated with information about changes since
the last release.

## 2. Bump the version

Use `bumpversion` (see
[bump-my-version](https://github.com/callowayproject/bump-my-version)) to bump
the specified part of the version:

```
$ bumpversion bump {major|minor|patch|prerelease|build|}
```

Versions should be in one of the following forms:

* `vX.Y.ZalphaN`: An alpha pre-release, e.g. `v1.2.3beta2`
* `vX.Y.ZbetaN`: A beta pre-release, e.g. `v1.2.3alpha2`
* `vX.Y.ZrcN`: A release candidate, e.g. `v1.2.3rc3`.
* `vX.Y.Z`: A final release, e.g. `v1.2.3`.

```{caution}
When using `bumpversion bump build`, ensure you have already used `bumpversion
bump prerelease`. Running `bumpversion bump build` from a final release version number
can result in an incorrect patch number, e.g. `v1.2.304`.
```

## 3. Create and push a git tag

Create a tag for the version. E.g.,:

```
git tag v4.0.0
```

Publishing the tag to GitHub will trigger an automated build of the `qgreenland`
Docker image via GitHub Actions.

```
git push origin v4.0.0
```

## 4. Build QGreenland

> [!NOTE] the official QGreenland package is built and distributed at NSIDC and
> currently can only be built by someone with access to the NSIDC VPN.

Connect to the NSIDC VPN and navigate to the [QGreenland
Jenkins](https://ci.qgreenland.apps.int.nsidc.org/). Use the
[qgreenland_C3_Production_Build_QGreenland_Package](https://ci.qgreenland.apps.int.nsidc.org/job/qgreenland_C3_Production_Build_QGreenland_Package/build?delay=0sec)
job to trigger a build with the git tag pushed above and wait for completion
(usually takes a little over an hour).


## 5. Create a GitHub release

Once a new version of the package has been successfully built and pushed to
mirrors, create a [new
release](https://github.com/nsidc/qgreenland/releases/new) in GitHub and add the
CHANGELOG for the new version in the release notes. If this is a pre-release
(e.g., `v4.0.0alpha3`), be sure to mark it as such!

Creating a new release will trigger archival of our code in Zenodo and issuance
of a new DOI. Do _not_ create a "Release" in GitHub until a new version of the
package has been successfully built and pushed to mirrors.

> [!WARNING] Creating a release in GitHub currently _does not_ archive our code
> on Zenodo or push anything to our mirrors. This is a TODO!
