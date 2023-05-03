BUILD_DIR     = _build
CHEATSHEETS   = pymapdl_cheat_sheet pyansys_cheat_sheet pyfluent_cheat_sheet pyaedt_API_cheat_sheet pyedb_API_cheat_sheet

.PHONY: all clean help

all: $(CHEATSHEETS)

pymapdl_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pymapdl_cheat_sheet.pdf $(BUILD_DIR)/pymapdl_cheat_sheet.png

pyansys_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/general_cheat_sheet_template/pyansys_general_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyansys_general_cheat_sheet.pdf $(BUILD_DIR)/pyansys_general_cheat_sheet.png

pyfluent_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/pyfluent_cheat_sheet/pyfluent_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyfluent_cheat_sheet.pdf $(BUILD_DIR)/pyfluent_cheat_sheet.png

pyaedt_API_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/aedt_cheat_sheet/pyaedt_API_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyaedt_API_cheat_sheet.pdf $(BUILD_DIR)/pyaedt_API_cheat_sheet.png

pyedb_API_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/aedt_cheat_sheet/pyedb_API_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyaedt_API_cheat_sheet.pdf $(BUILD_DIR)/pyaedt_API_cheat_sheet.png


clean:
	rm -rf $(BUILD_DIR)
	find . -type d -name "_autosummary" -exec rm -rf {} +

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)
