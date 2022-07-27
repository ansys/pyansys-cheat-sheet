BUILD = build

pymapdl_cheatsheat:
	latexmk -f -pdf -use-make cheat_sheats/mapdl_cheat_sheat/pymapdl_cheat_sheat.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true

pyaedt_cheatsheat:
	latexmk -f -pdf -use-make cheat_sheats/aedt_cheat_sheat/pyaedt_cheat_sheat.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true

pyansys_cheatsheat:
	latexmk -f -pdf -use-make cheat_sheat_template/pyansys_cheat_sheat.tex -cd -outdir=../$(BUILD) -interaction=nonstopmode || true

clean:
	rm -rf $(BUILD)

.PHONY: build clean

all: pymapdl_cheatsheat pyaedt_cheatsheat pyansys_cheatsheat