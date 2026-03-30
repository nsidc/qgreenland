# How to release a new version of QGreenland Core code


```{caution}
The official QGreenland package is built and distributed at NSIDC and
currently can only be built by someone with access to the NSIDC VPN. Most of
the steps shown here require collaboration with someone at NSIDC.
```

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


```{caution}
If datasets that were included in a previous release have been
updated and need to be re-fetched, ssh to the production VM and cleanup the
fetch cache for those datasets with the `clean` command to cleanup the
relevant datasets. E.g.,
`./scripts/cli.sh cleanup -f "caff_murre_colonies*"`
```

Connect to the NSIDC VPN and navigate to the [QGreenland
Jenkins](https://ci.qgreenland.apps.int.nsidc.org/). Use the
[qgreenland_C3_Production_Build_QGreenland_Package](https://ci.qgreenland.apps.int.nsidc.org/job/qgreenland_C3_Production_Build_QGreenland_Package/build?delay=0sec)
job to trigger a build with the git tag pushed above and wait for completion
(usually takes a little over an hour).

## 5. Update symlinks

The QGreenland package server provides two symlinks that can optionally be
updated as part of the release process. Once a new package has been build,
consider running one or both of the following Jenkins Jobs:

* [qgreenland_C4_Production_Update_Latest_Symlink/](https://ci.qgreenland.apps.int.nsidc.org/job/qgreenland_C4_Production_Update_Latest_Symlink/):
  Updates the ["latest"](https://nsidc.org/qgreenland/packages/latest/) symlink
  to the provided ref (e.g,. `dev/v4.0.0alpha3` or `v4.0.0`). Suitable for both
  pre-releases and official releases.

> [!NOTE] the ref for pre-release versions should start with `dev/`, followed by
> the version tag of the package you want to be marked as `latest`. This is
> because pre-releases exist under the
> [/dev](https://nsidc.org/qgreenland/packages/dev/) directory. In other words,
> if your pre-release tag is `v4.0.0alpha3`, the ref for this job should be
> `dev/v4.0.0alpha3`. For official releases, just the tag can be specified
> (e.g., `v4.0.0`)

* [qgreenland_C4_Production_Update_Stable_Symlink](https://ci.qgreenland.apps.int.nsidc.org/job/qgreenland_C4_Production_Update_Stable_Symlink/):
  Updates the ["stable"](https://nsidc.org/qgreenland/packages/stable/) symlink
  to the provided ref (e.g,. `v4.0.0`). Should only be used for official builds of
  QGreenland that have been tested and approved for release to the general
  public.


## 6. Create a GitHub release

Once a new version of the package has been successfully built, create a [new
release](https://github.com/nsidc/qgreenland/releases/new) in GitHub and add the
CHANGELOG for the new version in the release notes. If this is a pre-release
(e.g., `v4.0.0alpha3`), be sure to mark it as such!

Creating a new release will trigger archival of our code in Zenodo and issuance
of a new DOI. Do _not_ create a "Release" in GitHub until a new version of the
package has been successfully built.


## 7. Upload new version of package to Zenodo

Step 6 should have archived the code for QGreenland to Zenodo. For new official
(non-prerelease) versions of QGreenland, the finalized package should be
uploaded to Zenodo as a new version.

Login to Zenodo using the [QGreenland credentials in
Vault](https://vault.apps.int.nsidc.org:8200/ui/vault/secrets/nsidc/show/apps/qgreenland/zenodo)
and navigate to the [QGreenland data package
entry](https://zenodo.org/records/12823307). You should find a button "New
version" here that will initiate the process for uploading the package and
creating a new record.

## 8. Alert mirrors to new package availability

The QGreenland package is mirrored at the [Polar Geospatial
Center](https://www.pgc.umn.edu/) here:
<https://data.pgc.umn.edu/gis/packages/qgreenland/packages/>.

Once a new version of QGreenland is ready to be mirrored, reach out to the PGC
and request that they pull the latest data from our primary server here:
<https://nsidc.org/qgreenland/packages/>.

```{note}
The PGC does not typically mirror pre-releases. Only alert the PGC
once a version is ready for the general public (e.g., v4.0.0).
```
