SPHINXBUILD = sphinx-build
SOURCEDIR   = docs
BUILDDIR    = docs/_site
AUTOBUILD   = sphinx-autobuild

.PHONY: html clean livehtml

html:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" -W --keep-going
clean:
	rm -rf docs/_site docs/_build

livehtml:
	@$(AUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" \
		--host 0.0.0.0 --port 8000 \
		--open-browser
