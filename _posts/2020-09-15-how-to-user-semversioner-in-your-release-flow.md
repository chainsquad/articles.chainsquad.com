---
layout: post
title: How to use semversioner in your release flow
tags: semversion git flow
comments: true
---

Recently, we've marked a few of our branches in a project as *protected* which
results in local changes to the branch not being push-able to the remote branch.

This also means that when you are using [git
flow](https://danielkummer.github.io/git-flow-cheatsheet/), you need to come up
with a way to push your changes into a pull request and merge in the repo's frontend.

This lead me to believe that my readers would appreciate an article about how we use
[semantic versioning](https://semver.org/) in our release flow of python projects.

<!-- more -->

## Semversioner

`semversioner` is a tool that allows you to do updates to your code, document
them and have changelogs and version numbers generated automatically on release.

This is quite easy when you add a short method to your `.bashrc` or `.zshrc`:

```bash
def sem() {
  TYPE=$1  # patch, minor, major
  shift
  DESCRIPTION="$@"

  # Test git changes
  pre-commit run
  if [ $? -ne 0 ]; then
    return $?
  fi

  semversioner add-change --type ${TYPE} --description "${DESCRIPTION}"
  git add .changes

  git commit -m "${DESCRIPTION}"
}
```

After making a change to your source code, all you need to do is:

```
git add list-modified-files
sem patch|minor|major "Description of the change"
```

to have `semversioner` automatically deal with the change internally.
All the changes pending for the next release will be located in
`.changes/next-release` and `semversioner` will also deal with your release
numbering.

## Makefile

Together with the snippet above, we usually add the following to our Makefile
to make effective use of [git flow](https://danielkummer.github.io/git-flow-cheatsheet/):

```make
semver: semver-release semver-updates

semver-release:
	-semversioner release

semver-updates:
	semversioner changelog > CHANGELOG.md
	$(eval CURRENT_VERSION = $(shell semversioner current-version))
	sed -i "s/^__version__.*/__version__ = \"$(CURRENT_VERSION)\"/" setup.py
	-git add .changes setup.py CHANGELOG.md
	-git commit -m "semverioner release updates" --no-verify
	-git flow release start -F $(CURRENT_VERSION)
	-git flow release publish $(CURRENT_VERSION)
	git flow release finish -F -s -m "Release $(CURRENT_VERSION)" --noff-master --pushtag --pushdevelop --nopushproduction --keepremote --nokeeplocal $(CURRENT_VERSION)

release: semver clean build check
```

The `make release` does the following for your:

1. Create a new changelog and store it in `CHANGELOG.md`.
2. Obtain a new version number depending on the pending changes.
3. Update your `setup.py` to include the new `__version__`.
4. Commit the latest changes of `setup.py` and `CHANGELOG.md`.
5. Start a release flow with the new version number
6. Publish the new release branch
7. Finish the release

No, as you can see, the finishing of the release uses a bunch of options
`--noff-master --pushtag --pushdevelop --nopushproduction --keepremote
--nokeeplocal`. The sole purpose of those is to do be able to finish the
release locally, but not push it the remote as we have a **protected** `master`
branch.

After that, all that's left to do is to go to your repository management and
manually create a pull/merge request and have that merged into your production
branch.
