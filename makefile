BUILD = build

pymapdl_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true

pyaedt_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheets/aedt_cheat_sheet/pyaedt_cheat_sheet.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true

pyansys_cheat_sheet:
	latexmk -f -pdf -use-make cheat_sheet_template/general_cheat_sheet_template/pyansys_cheat_sheet.tex -cd -outdir=../$(BUILD) -interaction=nonstopmode || true

clean:
	rm -rf $(BUILD)

.PHONY: build clean

all: pymapdl_cheat_sheet pyaedt_cheat_sheet pyansys_cheat_sheet