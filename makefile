BUILD_DIR     = _build
CHEATSHEETS   = pymapdl_cheat_sheet pyfluent_cheat_sheet pyaedt_API_cheat_sheet pyedb_API_cheat_sheet pyprimemesh_cheat_sheet

.PHONY: all clean help

all: $(CHEATSHEETS)

pymapdl_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pymapdl_cheat_sheet.pdf $(BUILD_DIR)/pymapdl_cheat_sheet.png

pyfluent_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/pyfluent_cheat_sheet/pyfluent_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyfluent_cheat_sheet.pdf $(BUILD_DIR)/pyfluent_cheat_sheet.png

pyaedt_API_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/aedt_cheat_sheet/pyaedt_API_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyaedt_API_cheat_sheet.pdf $(BUILD_DIR)/pyaedt_API_cheat_sheet.png

pyedb_API_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/aedt_cheat_sheet/pyedb_API_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyedb_API_cheat_sheet.pdf $(BUILD_DIR)/pyedb_API_cheat_sheet.png

pyprimemesh_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/pyprimemesh_cheat_sheet/pyprimemesh_cheat_sheet.tex -cd -outdir=../../$(BUILD_DIR) -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyprimemesh_cheat_sheet.pdf $(BUILD_DIR)/pyprimemesh_cheat_sheet.png

clean:
	rm -rf $(BUILD_DIR)

help:
	@echo "Available targets:"
	@echo "  all:         Build all cheat sheets"
	@echo "  clean:       Remove the build directory and temporary files"
	@echo "  help:        Show this help message"
	@echo ""
	@echo "Individual Cheat Sheet Targets:"
	@echo "  pymapdl_cheat_sheet:       Build the pymapdl cheat sheet"
	@echo "  pyfluent_cheat_sheet:      Build the pyfluent cheat sheet"
	@echo "  pyaedt_API_cheat_sheet:    Build the pyaedt API cheat sheet"
	@echo "  pyedb_API_cheat_sheet:     Build the pyedb API cheat sheet"
	@echo "  pyprimemesh_cheat_sheet:   Build the pyprimemesh cheat sheet"
	
