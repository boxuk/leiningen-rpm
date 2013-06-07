
# Leiningen RPM

This repository contains a spec file which will build an RPM for a specific
version of Leiningen.  The package will be named 'boxuk-leiningen' to avoid
naming conflicts should an official pakcage become available and supported.

## Usage

To update to new versions of Leiningen you should just need to update the
*_lein_version* %define in the spec file, then create a new annotated tag
and start the build.

```
git describe # show latest tag
git tag -a XXX -m 'message'
git push --tags
```

Then after running the build on Jenkins the package will be available in
the unstable Box UK repo.

