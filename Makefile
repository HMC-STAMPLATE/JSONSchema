SPHINXBUILD = sphinx-build
SOURCEDIR   = docs
BUILDDIR    = docs/_site

.PHONY: html clean

html:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" -W --keep-going
clean:
	rm -rf docs/_site docs/_build
