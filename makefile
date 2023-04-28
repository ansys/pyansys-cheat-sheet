BUILD_DIR     = _build
CHEATSHEETS   = pymapdl_cheat_sheet pyaedt_cheat_sheet pyansys_cheat_sheet pyfluent_cheat_sheet

.PHONY: all clean help

all: $(CHEATSHEETS)

pymapdl_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true

pyaedt_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/aedt_cheat_sheet/pyaedt_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true

pyansys_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/general_cheat_sheet_template/pyansys_general_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true

pyfluent_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/pyfluent_cheat_sheet/pyfluent_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true

clean:
	rm -rf $(BUILD_DIR)
	find . -type d -name "_autosummary" -exec rm -rf {} +

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)
