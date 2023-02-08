# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
BUILD_DIR     = _build
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)
	
# customized clean due to api examples
clean:
	rm -rf $(BUILD_DIR)
	find . -type d -name "_autosummary" -exec rm -rf {} +