BUILD_DIR     = _build

CHEATSHEETS   = pymapdl_cheat_sheet pyfluent_cheat_sheet pyaedt_API_cheat_sheet pyedb_API_cheat_sheet pyprimemesh_cheat_sheet pydpf-core_cheat_sheet pymechanical_cheat_sheet


.PHONY: all clean help

all: $(CHEATSHEETS)

pymapdl_cheat_sheet:
	latexmk -f -pdf -use-make -outdir=$(BUILD_DIR) cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex  -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pymapdl_cheat_sheet.pdf $(BUILD_DIR)/pymapdl_cheat_sheet.png
	(test -f $(BUILD_DIR)/pymapdl_cheat_sheet.pdf && echo pdf exists) || exit 1

pyfluent_cheat_sheet:
	make run_script SCRIPT_PATH='cheat_sheets/pyfluent_cheat_sheet/pyfluent_script.py'
	latexmk -f -pdf -use-make -outdir=$(BUILD_DIR) cheat_sheets/pyfluent_cheat_sheet/pyfluent_cheat_sheet.tex -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyfluent_cheat_sheet.pdf $(BUILD_DIR)/pyfluent_cheat_sheet.png
	(test -f $(BUILD_DIR)/pyfluent_cheat_sheet.pdf && echo pdf exists) || (echo "Failed to generate PDF" && exit 1)

pyaedt_API_cheat_sheet:
	latexmk -f -pdf -use-make -outdir=$(BUILD_DIR) cheat_sheets/aedt_cheat_sheet/pyaedt_API_cheat_sheet.tex -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyaedt_API_cheat_sheet.pdf $(BUILD_DIR)/pyaedt_API_cheat_sheet.png
	(test -f $(BUILD_DIR)/pyaedt_API_cheat_sheet.pdf && echo pdf exists) || exit 1

pyedb_API_cheat_sheet:
	latexmk -f -pdf -use-make -outdir=$(BUILD_DIR) cheat_sheets/aedt_cheat_sheet/pyedb_API_cheat_sheet.tex -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyedb_API_cheat_sheet.pdf $(BUILD_DIR)/pyedb_API_cheat_sheet.png
	(test -f $(BUILD_DIR)/pyedb_API_cheat_sheet.pdf && echo pdf exists) || exit 1

pyprimemesh_cheat_sheet:
	latexmk -f -pdf -use-make -outdir=$(BUILD_DIR) cheat_sheets/pyprimemesh_cheat_sheet/pyprimemesh_cheat_sheet.tex -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pyprimemesh_cheat_sheet.pdf $(BUILD_DIR)/pyprimemesh_cheat_sheet.png
	(test -f $(BUILD_DIR)/pyprimemesh_cheat_sheet.pdf && echo pdf exists) || exit 1

pydpf-core_cheat_sheet:
	latexmk -f -pdf -use-make -outdir=$(BUILD_DIR) cheat_sheets/pydpf-core_cheat_sheet/pydpf-core_cheat_sheet.tex -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pydpf-core_cheat_sheet.pdf $(BUILD_DIR)/pydpf-core_cheat_sheet.png
	(test -f $(BUILD_DIR)/pydpf-core_cheat_sheet.pdf && echo pdf exists) || exit 1

pymechanical_cheat_sheet:
	make run_script SCRIPT_PATH='cheat_sheets/pymechanical_cheat_sheet/pymechanical_script.py'
	latexmk -f -pdf -use-make -outdir=$(BUILD_DIR) cheat_sheets/pymechanical_cheat_sheet/pymechanical_cheat_sheet.tex -interaction=nonstopmode || true
	convert -density 150 -scene 1 $(BUILD_DIR)/pymechanical_cheat_sheet.pdf $(BUILD_DIR)/pymechanical_cheat_sheet.png
	(test -f $(BUILD_DIR)/pymechanical_cheat_sheet.pdf && echo pdf exists) || (echo "Failed to generate PDF" && exit 1)
    
run_script:
	python3 scripts/generate_code_snippet.py $(SCRIPT_PATH)

clean:
	rm -rf $(BUILD_DIR)

help:
	@echo "Available targets:"
	@echo "  all:         Build all cheatsheets"
	@echo "  clean:       Remove the build directory and temporary files"
	@echo "  help:        Show this help message"
	@echo ""
	@echo "Individual cheatsheet Targets:"
	@echo "  pymapdl_cheat_sheet:       Build the pymapdl cheatsheet"
	@echo "  pyfluent_cheat_sheet:      Build the pyfluent cheatsheet"
	@echo "  pyaedt_API_cheat_sheet:    Build the pyaedt API cheatsheet"
	@echo "  pyedb_API_cheat_sheet:     Build the pyedb API cheatsheet"
	@echo "  pyprimemesh_cheat_sheet:   Build the pyprimemesh cheatsheet"
	@echo "  pymechanical_cheat_sheet:   Build the pymechanical cheatsheet"
	
