BUILD = build

pymapdl_cheatsheat:
	latexmk -f -pdf -use-make mapdl_cheat_sheat/pymapdl_cheat_sheat.tex -cd -outdir=../$(BUILD) -interaction=nonstopmode || true

pyaedt_cheatsheat:
	latexmk -f -pdf -use-make aedt_cheat_sheat/pyaedt_cheat_sheat.tex -cd -outdir=../$(BUILD) -interaction=nonstopmode || true


clean:
	rm -rf $(BUILD)

.PHONY: build clean